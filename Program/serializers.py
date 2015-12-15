from rest_framework import serializers
from Program.models import BaseExercise, MuscleGroup, Program, Week, Day, Exercise
from django.contrib.auth.models import User

class MuscleGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id', 'name')

		

class BaseExerciseSerializer(serializers.ModelSerializer):
	muscle_group = MuscleGroupSerializer()
	class Meta:
		model = BaseExercise
		fields = ('id', 'name', 'youtube_link', 'muscle_group', 'description')




class ExerciseSerializer(serializers.ModelSerializer):
	base_exercise = BaseExerciseSerializer(read_only=True)
	class Meta:
		model = Exercise
		fields = ('id', 'set', 'reps', 'day', 'description', 'break_time','base_exercise')


class ExerciseEditSerializer(serializers.ModelSerializer):
	#base_exercise = serializers.PrimarKeyRelatedField(read_only=False)
	class Meta:
		model = Exercise
		fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
	exercises = ExerciseSerializer(many=True, read_only=True)
	class Meta:
		model = Day
		fields = ('id', 'name', 'week', 'exercises')
	

class WeekSerializer(serializers.ModelSerializer):

	days = DaySerializer(many=True, read_only=True)

	class Meta:
		model = Week
		fields = ('id', 'name', 'program', 'days')





class ProgramSerializer(serializers.ModelSerializer):
	weeks = WeekSerializer(many=True, read_only=True)

	class Meta:
		model = Program
		fields = ('id', 'name', 'date', 'user', 'weeks')


	def __unicode__(self):
		return "%s-%s-%s" %(self.name, self.date, self.user)

class WorkoutProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = Program
		fields = '__all__'

class WorkoutWeekSerializer(serializers.ModelSerializer):
	program = WorkoutProgramSerializer(many=False, read_only=True)
	class Meta:
		model = Week
		fields = ('id', 'name', 'program', 'days')

class WorkoutDaySerializer(serializers.ModelSerializer):
	week = WorkoutWeekSerializer(many=False, read_only=True)
	class Meta:
		model = Day
		fields = ('id', 'name', 'week', 'exercises')

class WorkoutBaseExerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseExercise
		fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
	base_exercise = WorkoutBaseExerciseSerializer(many=False, read_only=True)
	class Meta:
		model = Exercise
		fields = '__all__'



