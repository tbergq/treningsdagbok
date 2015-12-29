from rest_framework.views import APIView
from rest_framework.response import Response
 
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
 
from django.contrib.auth.models import User
from Account.models import UserReset
from Account.serializers import UserSerializer, UserResetSerializer
from rest_framework import generics
from django.contrib.auth import hashers
import uuid
import datetime
from Account.mailService import MailService
 
 
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



class PasswordReset(APIView):
	def get(self, request, format=None):
		email = request.query_params.get('email', None)
		redirect_url = request.query_params.get('redirect_url', None)
		if email != None:
			user = User.objects.get(email=email)
			reset = UserReset(user_id=user.id, guid=uuid.uuid1(), reset_time=datetime.datetime.now())
			reset.save()
			redirect_url = "%s%s" % (redirect_url, reset.guid)
			message = "got to %s to reset password" % redirect_url
			MailService().send_mail(email, message)
			return Response({}, status.HTTP_200_OK)
		return Response({'error' : 'no mail address supplied'}, status.HTTP_400_BAD_REQUEST)


	def post(self, request, format=None):
		reset = UserReset.objects.get(guid=request.data['guid'])
		reset_time = reset.reset_time.replace(tzinfo=None)
		now = datetime.datetime.now()
		delta = now - reset_time

		if delta.days > 1:
			reset.delete()
			return Response({'error' : 'reset token to old'}, status.HTTP_400_BAD_REQUEST)
			
		user = User.objects.get(pk=reset.user_id)
		encoded_password = hashers.make_password(request.data['new_password'])
		if hashers.is_password_usable(encoded_password):
			user.password = encoded_password
			user.save()
			reset.delete()
			return Response({}, status.HTTP_200_OK)
		return Response({'error' : 'reset passoword failed'}, status.HTTP_400_BAD_REQUEST)













