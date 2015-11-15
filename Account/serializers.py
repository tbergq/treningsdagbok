from rest_framework import serializers
#from Account.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()

	def create(self, validated_data):
		user = User(email=validated_data['email'], username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User#Profile
		fields = ('id', 'username', 'password', 'email')