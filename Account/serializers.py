from rest_framework import serializers
#from Account.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import Account.models as account_models

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

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email')


class UserResetSerializer(serializers.ModelSerializer):
	class Meta:
		model = account_models.UserReset
		fields = '__all__'
	