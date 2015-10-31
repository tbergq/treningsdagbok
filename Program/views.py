from rest_framework import generics
from Program.models import BaseExercise
from Program.serializers import BaseExerciseSerializer

class BaseExerciseList(generics.ListCreateAPIView):
	queryset = BaseExercise.objects.all()
	serializer_class = BaseExerciseSerializer