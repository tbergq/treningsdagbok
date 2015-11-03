from rest_framework import generics, mixins
from Program.models import BaseExercise, MuscleGroup, Program
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Program.serializers import BaseExerciseSerializer, MuscleGroupSerializer, ProgramSerializer
from django.shortcuts import render, get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status

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

	def post(self, request, format=None):
		print "post program list"
		#serializer = ProgramSerializer(data=request.data)
		date_now = datetime.datetime.now()
		req = request.data
		print request.user.id
		user_profile = User.objects.get(pk=request.user.id)
		program = Program(name=req["name"], date=date_now, user=user_profile)
		program.save()
		serializer = ProgramSerializer(program)
		#serializer.date = datetime.datetime.now()
		#serializer.user = request.user.id
		#print serializer.name
		#print serializer.date
		#print serializer.user
		#if serializer.is_valid():
		#serializer.save()
		return Response(serializer.data)
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer




