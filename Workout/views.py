from rest_framework import generics, mixins
from rest_framework.views import APIView
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exercise
from Workout.models import DayRegister
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Program.serializers import BaseExerciseSerializer, MuscleGroupSerializer, ProgramSerializer, WeekSerializer, DaySerializer, ExerciseSerializer
from Workout.serializers import DayRegisterSerializer, ExcerciseSerializer, ExcerciseWithForeignSerializer, DayRegisterCustomSerializer, ExerciseCustomSerializer, ExcerciseDepthTwoSerializer, OtherActivitySerializer
from django.shortcuts import render, get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status
#from Program import services
from rest_framework.permissions import IsAuthenticated
import Workout.services as workout_services
import Workout.models as workout_models

class OtherActivityList(generics.ListCreateAPIView):
	#queryset = BaseExercise.objects.all()
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
	#queryset = BaseExercise.objects.all()
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
	#queryset = Day.objects.all()

	def get_queryset(self):
		day_id = self.kwargs["day_id"]
		queryset = DayRegister.objects.filter(day_program_id=day_id)
		return queryset

	def post(self, request, day_id, format=None):
		print "post"
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
		print "update"
		data = request.data
		print kwargs
		item = workout_models.DayRegister.objects.get(pk=kwargs["pk"])
		item.end_time = datetime.datetime.now()
		item.save()
		serializer = DayRegisterSerializer(item)
		return Response(serializer.data, status.HTTP_200_OK)


class ExcerciseRegisterList(generics.ListCreateAPIView):
	serializer_class = ExcerciseSerializer
	#queryset = workout_models.ExcerciseRegister.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		day_register_id = self.request.query_params.get('day_register_id', None)
		day_excersice_id = self.request.query_params.get('day_excersice_id', None)

		return workout_models.ExcerciseRegister.objects.filter(day_excersice_id=day_excersice_id, day_register_id=day_register_id)
		


class GetLastRegisteredList(generics.ListCreateAPIView):

	serializer_class = ExcerciseWithForeignSerializer
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		print "get latest registered"
		user_id = request.user.id
		day_register_id = request.query_params.get('day_register_id', None)
		base_exercise_id = request.query_params.get('base_exercise_id', None)
		registers = workout_services.WorkoutManager().get_latest_registers(user_id, day_register_id, base_exercise_id)
		data = []
		for item in registers:
			temp_item = {'reps' : item.reps, 'weight' : item.weight}
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
		registers = workout_services.WorkoutManager().get_day_registers_from_program_id(program_id)
		#print "got registers"
		#print registers
		#test = DayRegisterCustomSerializer(registers[0])
		#print test.data
		serializer = DayRegisterCustomSerializer(registers, many=True)
		return Response(serializer.data, status.HTTP_200_OK)


class ExcerciseRegisterDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ExcerciseDepthTwoSerializer
	queryset = workout_models.ExcerciseRegister.objects.all()





