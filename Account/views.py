from rest_framework.views import APIView
from rest_framework.response import Response
 
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
 
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Account.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth import hashers
 
 
# Create your views here.


class UserView(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def post(self, request, format=None):
		print "user post"
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save();
			#UserProfile.create_new(serializer.id)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListCreateAPIView):
	serializer_class = UserSerializer

	def get_queryset(self):
		return None

class UserInfoView(APIView):

	def get(self, request, format=None):
		user = User.objects.get(pk=request.user.id)
		user_data = {'username' : user.username, 'email' : user.email}
		return Response(user_data, status.HTTP_200_OK)


class ChangePassword(APIView):
	
	def post(self, request, format=None):
		user = User.objects.get(pk=request.user.id)
		old_password = request.data['old_password']
		
		if user.check_password(old_password):
			new_password = request.data['new_password']
			encoded_password = hashers.make_password(new_password)
			if hashers.is_password_usable(encoded_password):
				user.password = encoded_password
				user.save()
				return Response({}, status.HTTP_200_OK)
		else:
			return Response({}, status.HTTP_400_BAD_REQUEST)
		return None
















