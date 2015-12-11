from rest_framework import generics, mixins
from rest_framework.views import APIView
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exercise
from Workout.models import DayRegister
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Program.serializers import BaseExerciseSerializer, MuscleGroupSerializer, ProgramSerializer, WeekSerializer, DaySerializer, ExerciseSerializer
from Workout.serializers import DayRegisterSerializer, ExcerciseSerializer, ExcerciseWithForeignSerializer
from django.shortcuts import render, get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status
#from Program import services
from rest_framework.permissions import IsAuthenticated
import Workout.services as workout_services
import Workout.models as workout_models

"""class BaseExerciseList(generics.ListCreateAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer
	permission_classes = (IsAuthenticated,)
	

class BaseExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer
	permission_classes = (IsAuthenticated,)"""


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







