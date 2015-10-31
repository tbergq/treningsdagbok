from rest_framework import serializers
from Accout.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('id', 'username', 'password', 'email')