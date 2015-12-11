from rest_framework import serializers
import Program.models as program_models
import Workout.models as workout_models
from django.contrib.auth.models import User
import Program.serializers as program_serializers

class DayRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = workout_models.DayRegister
		fields = '__all__'


class ExcerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = '__all__'

class ExcerciseWithForeignSerializer(serializers.ModelSerializer):
	day_excersice = program_serializers.ExerciseSerializer(many=True, read_only=True)
	day_register = DayRegisterSerializer(many=True, read_only=True)
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = ('day_excersice', 'day_register', 'set_number ', 'reps', 'weight', 'note') 
     
