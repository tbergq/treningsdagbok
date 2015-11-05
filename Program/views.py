from rest_framework import generics, mixins
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exersice
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Program.serializers import BaseExerciseSerializer, MuscleGroupSerializer, ProgramSerializer, WeekSerializer, DaySerializer, ExerciseSerializer
from django.shortcuts import render, get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status
from Program import services

class BaseExerciseList(generics.ListCreateAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer

	

class BaseExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer


class MuscleGroupList(generics.ListCreateAPIView):
	queryset = MuscleGroup.objects.all()
	serializer_class = MuscleGroupSerializer

	

class MuscleGroupDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MuscleGroup.objects.all()
	serializer_class = MuscleGroupSerializer

class ProgramList(generics.ListCreateAPIView):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer

	def get(self, request, format=None):
		serializer = ProgramSerializer(Program.objects.filter(user_id=request.user.id), many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		print "post program list"
		date_now = datetime.datetime.now()
		req = request.data
		print request.user.id
		user_profile = User.objects.get(pk=request.user.id)
		program = Program(name=req["name"], date=date_now, user=user_profile)
		program.save()
		serializer = ProgramSerializer(program)
		return Response(serializer.data)


class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer

	


class WeekGroupList(generics.ListCreateAPIView):
	queryset = Week.objects.all()
	serializer_class = WeekSerializer



	""""def post(self, request, format=None):
		serializer = WeekSerializer(data=request.data)
		if serializer.is_valid():
			print "valid"
		else:
			print serializer.errors"""


