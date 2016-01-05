from rest_framework import generics, mixins
from rest_framework.views import APIView
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exercise
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Program.serializers import BaseExerciseSerializer, MuscleGroupSerializer, ProgramSerializer, WeekSerializer, DaySerializer, ExerciseSerializer, ExerciseEditSerializer
from django.shortcuts import render, get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status
from Program import services
from rest_framework.permissions import IsAuthenticated
from Program.permissions import IsSuperUser

class BaseExerciseList(generics.ListCreateAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		data = request.data;
		print data
		item = BaseExercise(muscle_group_id=data["muscle_group"], name=data["name"], youtube_link=data["youtube_link"], description=data["description"])
		item.save()
		serializer = BaseExerciseSerializer(item)
		return Response(serializer.data, status.HTTP_201_CREATED)
	

class BaseExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer
	permission_classes = (IsAuthenticated, IsSuperUser)

	def update(self, request, *args, **kwargs):
		data = request.data
		print data
		item = BaseExercise.objects.get(pk=data["id"])
		item.description = data["description"]
		item.muscle_group_id = data["muscle_group"]["id"]
		item.name = data["name"]
		item.youtube_link = data["youtube_link"]
		item.save()
		serializer = BaseExerciseSerializer(item)
		return Response(serializer.data, status.HTTP_200_OK)




class MuscleGroupList(generics.ListCreateAPIView):
	queryset = MuscleGroup.objects.all()
	serializer_class = MuscleGroupSerializer
	permission_classes = (IsAuthenticated,)

	

class MuscleGroupDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MuscleGroup.objects.all()
	serializer_class = MuscleGroupSerializer
	permission_classes = (IsAuthenticated,)

class ProgramList(generics.ListCreateAPIView):
	queryset = Program.objects.order_by('id')
	serializer_class = ProgramSerializer
	permission_classes = (IsAuthenticated,)


	"""def get(self, request, format=None):
		serializer = ProgramSerializer(Program.objects.filter(user_id=request.user.id), many=True)
		return Response(serializer.data)"""


	def post(self, request, format=None):
		print "post program list"
		date_now = datetime.datetime.now()
		req = request.data
		print request.user.id
		user_profile = User.objects.get(pk=request.user.id)
		program = Program(name=req["name"], date=date_now, user=user_profile)
		program.save()
		serializer = ProgramSerializer(program)
		return Response(serializer.data, status.HTTP_201_CREATED)

	def get_queryset(self):
		#user = self.request.user
		return Program.objects.filter(user_id=self.request.user.id).order_by('-date')


class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Program.objects.all()
	serializer_class = ProgramSerializer
	permission_classes = (IsAuthenticated,)




class WeekGroupList(generics.ListCreateAPIView):
	queryset = Week.objects.all()
	serializer_class = WeekSerializer
	permission_classes = (IsAuthenticated,)

class WeekDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Week.objects.all()
	serializer_class = WeekSerializer
	permission_classes = (IsAuthenticated,)

class DayGroupList(generics.ListCreateAPIView):
	queryset = Day.objects.all()
	serializer_class = DaySerializer
	permission_classes = (IsAuthenticated,)

class DayDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Day.objects.all()
	serializer_class = DaySerializer
	permission_classes = (IsAuthenticated,)


class ExerciseGroupList(generics.ListCreateAPIView):
	queryset = Exercise.objects.all()
	serializer_class = ExerciseSerializer
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		data = request.data
		item = Exercise(base_exercise_id=data["base_exercise"], set=data["set"], reps=data["reps"], day_id=data["day"], description=data["description"], break_time=data["break_time"])
		item.save()
		serializer = ExerciseSerializer(item)
		return Response(serializer.data, status.HTTP_201_CREATED)

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Exercise.objects.all()
	serializer_class = ExerciseEditSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		print self.request.data
		return Exercise.objects.all()


class CopyWeek(APIView):
	permission_classes = (IsAuthenticated,)
	
	def post(self, request, week_id, format=None):
		new_week_id = services.WeekService().copy_week_from_week_id(week_id)
		serializer = WeekSerializer(Week.objects.get(pk=new_week_id))
		return Response(serializer.data, status.HTTP_201_CREATED)
	


