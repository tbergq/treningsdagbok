from rest_framework import serializers
import Program.models as program_models
import Workout.models as workout_models
from django.contrib.auth.models import User

class DayRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = workout_models.DayRegister
		fields = '__all__'


class ExcerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = '__all__'
