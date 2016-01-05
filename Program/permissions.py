from rest_framework import permissions
from django.contrib.auth.models import User


class IsSuperUser(permissions.BasePermission):


	def has_permission(self, request, view):
		if request.method == 'PUT' or request.method == 'DELETE':
			user = User.objects.get(pk=request.user.id)
			return user.is_superuser;
		else:
			return True