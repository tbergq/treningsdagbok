from rest_framework.views import APIView
from rest_framework.response import Response
 
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
 
from django.contrib.auth.models import User
 
 
# Create your views here.
class AuthView(APIView):
	"""
	Authentication is needed for this methods
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		return Response({'detail': "I suppose you are authenticated"})