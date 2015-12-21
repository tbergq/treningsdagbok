from rest_framework import serializers
import Program.models as program_models
import Workout.models as workout_models
from django.contrib.auth.models import User
import Program.serializers as program_serializers

class DayRegisterSerializer(serializers.ModelSerializer):
	#day_program = program_serializers.DaySerializer(many=True, read_only=True)
	class Meta:
		model = workout_models.DayRegister
		fields = '__all__'


class ExcerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = '__all__'
		#depth = 2

class ExcerciseWithForeignSerializer(serializers.ModelSerializer):
	day_excersice = program_serializers.ExerciseSerializer(many=True, read_only=True)
	day_register = DayRegisterSerializer(many=True, read_only=True)
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = ('day_excersice', 'day_register', 'set_number ', 'reps', 'weight', 'note') 
     

class DayRegisterCustomSerializer(serializers.ModelSerializer):
	day_program = program_serializers.WorkoutDaySerializer(many=False, read_only=True)
	class Meta:
		model = workout_models.DayRegister
		fields = ('id', 'start_time', 'end_time', 'day_program', 'user')

class ExerciseCustomSerializer(serializers.ModelSerializer):
	day_excersice = program_serializers.WorkoutExerciseSerializer(many=False, read_only=True)
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = ('id', 'day_excersice', 'set_number', 'reps', 'weight', 'note')

class ExcerciseDepthTwoSerializer(serializers.ModelSerializer):
	class Meta:
		model = workout_models.ExcerciseRegister
		fields = '__all__'
		depth = 2

class OtherActivitySerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source="user.id")
	#description = serializers.CharField(blank=True)
	class Meta:
		model = workout_models.OtherActivity
		fields = '__all__'





