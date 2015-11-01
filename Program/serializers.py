from rest_framework import serializers
from Program.models import BaseExercise, MuscleGroup, Program

class BaseExerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseExercise
		fields = ('id', 'name', 'youtube_link', 'muscle_group', 'description')


class MuscleGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id', 'name')

class ProgramSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Program
		fields = ('id', 'name', 'date', 'user')