from rest_framework import serializers
#from Account.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User#Profile
		fields = ('id', 'username', 'password', 'email')