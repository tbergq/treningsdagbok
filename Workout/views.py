from rest_framework import generics, mixins
from rest_framework.views import APIView
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exercise
from Workout.models import DayRegister
from django.contrib.auth.models import User
from Program.serializers import BaseExerciseSerializer, MuscleGroupSerializer, ProgramSerializer, WeekSerializer 
from Program.serializers import DaySerializer, ExerciseSerializer
from Workout.serializers import DayRegisterSerializer, ExcerciseSerializer, ExcerciseWithForeignSerializer
from Workout.serializers import DayRegisterCustomSerializer, ExerciseCustomSerializer, ExcerciseDepthTwoSerializer
from Workout.serializers import OtherActivitySerializer, OneRepMaxSerializer
from django.shortcuts import render, get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import Workout.services as workout_services
import Workout.models as workout_models

class OtherActivityList(generics.ListCreateAPIView):
	serializer_class = OtherActivitySerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		start = self.request.query_params.get('start', None)
		end = self.request.query_params.get('end', None)
		if start != None and end != None:
			start = datetime.datetime.fromtimestamp(float(start))
			end = datetime.datetime.fromtimestamp(float(end))
			return workout_models.OtherActivity.objects.filter(user_id=self.request.user.id, date__gte=start, date__lte=end)
		return workout_models.OtherActivity.objects.filter(user_id=self.request.user.id)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
	

class OtherActivityDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = OtherActivitySerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return workout_models.OtherActivity.objects.filter(user_id=self.request.user.id)

class RegisterDayAllForUserList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = DayRegisterCustomSerializer

	
	def get_queryset(self):
		start = self.request.query_params.get('start', None)
		end = self.request.query_params.get('end', None)
		
		if start != None and end != None:
			start_time = datetime.datetime.fromtimestamp(float(start))
			end_time = datetime.datetime.fromtimestamp(float(end))
			return DayRegister.objects.exclude(end_time__isnull=True).filter(user_id=self.request.user.id, end_time__lte=end_time, start_time__gte=start_time).order_by('-start_time')
		
		return DayRegister.objects.filter(user_id=self.request.user.id).exclude(end_time__isnull=True).order_by('-start_time')


class RegisterDayList(generics.ListCreateAPIView):
	serializer_class = DayRegisterSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		day_id = self.kwargs["day_id"]
		queryset = DayRegister.objects.filter(day_program_id=day_id, user_id=self.request.user.id)
		return queryset

	def post(self, request, day_id, format=None):
		date_now = datetime.datetime.now()
		req = request.data
		user_profile = User.objects.get(pk=request.user.id)
		register = workout_models.DayRegister(day_program_id=day_id, start_time=date_now, user=user_profile)
		register.save()
		serializer = DayRegisterSerializer(register)
		return Response(serializer.data, status.HTTP_201_CREATED)

class RegisterDayDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = DayRegisterSerializer
	permission_classes = (IsAuthenticated,)
	queryset = Day.objects.all()

	def update(self, request, *args, **kwargs):
		data = request.data
		item = workout_models.DayRegister.objects.get(pk=kwargs["pk"])
		item.end_time = datetime.datetime.now()
		item.save()
		serializer = DayRegisterSerializer(item)
		return Response(serializer.data, status.HTTP_200_OK)


class ExcerciseRegisterList(generics.ListCreateAPIView):
	serializer_class = ExcerciseSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		day_register_id = self.request.query_params.get('day_register_id', None)
		day_excersice_id = self.request.query_params.get('day_excersice_id', None)

		return workout_models.ExcerciseRegister.objects.filter(day_excersice_id=day_excersice_id, day_register_id=day_register_id)
		


class GetLastRegisteredList(generics.ListCreateAPIView):

	serializer_class = ExcerciseWithForeignSerializer
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		user_id = request.user.id
		day_register_id = request.query_params.get('day_register_id', None)
		base_exercise_id = request.query_params.get('base_exercise_id', None)
		registers = workout_services.WorkoutManager().get_latest_registers(user_id, day_register_id, base_exercise_id)
		data = []
		for item in registers:
			temp_item = {'reps' : item.reps, 'weight' : item.weight, 'note' : item.note}
			data.append(temp_item)
		return Response(data, status.HTTP_200_OK)




class ExcerciseRegisterForDayRegister(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ExerciseCustomSerializer

	def get_queryset(self):
		day_register_id = self.kwargs["day_register_id"]
		return workout_models.ExcerciseRegister.objects.filter(day_register_id=day_register_id, day_register__user_id=self.request.user.id)



class DayRegisterOfProgram(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, program_id, format=None):
		registers = workout_services.WorkoutManager().get_day_registers_from_program_id(program_id, request.user.id)
		serializer = DayRegisterCustomSerializer(registers, many=True)
		return Response(serializer.data, status.HTTP_200_OK)


class ExcerciseRegisterDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ExcerciseDepthTwoSerializer
	queryset = workout_models.ExcerciseRegister.objects.all()




class OneRepMaxList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = OneRepMaxSerializer

	def get_queryset(self):
		latest = self.request.query_params.get('latest', None)
		base_exercise_id = self.request.query_params.get('base_exercise_id', None)

		if latest != None and latest:
			return workout_services.OneRepMaxService().get_latest(self.request.user.id)
		elif base_exercise_id != None:
			return workout_models.OneRepMax.objects.filter(user_id=self.request.user.id, base_exercise_id=base_exercise_id).order_by('date')
		return workout_models.OneRepMax.objects.filter(user_id=self.request.user.id)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, base_exercise_id=self.request.data["base_exercise_id"])



























