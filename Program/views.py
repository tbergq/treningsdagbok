from rest_framework import generics, mixins
from Program.models import BaseExercise, MuscleGroup, Program
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
		serializer = ProgramSerializer(data=request.data)
		serializer.date = datetime.datetime.now()
		serializer.user = request.user.id
		print serializer.date
		print serializer.user
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer




