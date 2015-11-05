from rest_framework import serializers
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exersice

class BaseExerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseExercise
		fields = ('id', 'name', 'youtube_link', 'muscle_group', 'description')


class MuscleGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id', 'name')



	

class WeekSerializer(serializers.ModelSerializer):

	class Meta:
		model = Week
		fields = ('id', 'name', 'program')

class DaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Day
		fields = ('id', 'name')

class ExerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exersice
		fields = ('id', 'set', 'reps', 'day', 'description', 'break_time')

class ProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = Program
		fields = ('id', 'name', 'date', 'user', 'weeks')

	weeks = WeekSerializer(many=True, read_only=True)#serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	def __unicode__(self):
		return "%s-%s-%s" %(self.name, self.date, self.user)