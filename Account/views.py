from rest_framework.views import APIView
from rest_framework.response import Response
 
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
 
from django.contrib.auth.models import User
#from Account.models import UserProfile
from Account.serializers import UserSerializer
from rest_framework import generics
 
 
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
