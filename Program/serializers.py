from rest_framework import serializers
from Program.models import BaseExercise

class BaseExerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseExercise
		fields = ('id', 'name', 'youtube_link', 'muscle_group')
