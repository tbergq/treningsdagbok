from rest_framework import permissions
import Groups.models as group_models


class IsGroupOwner(permissions.BasePermission):


	def has_permission(self, request, view):
		if request.method == 'PUT' or request.method == 'DELETE':
			return group_models.Group.objects.get(pk=view.kwargs["pk"]).owner_id == request.user.id
		else:
			return True


class IsGroupMemberOrOwner(permissions.BasePermission):

	def has_permission(self, request, view):
		group_id=request.query_params.get('groupId', 0)
		user_id=request.user.id
		is_group_owner = group_models.Group.objects.filter(group_owner_id=user_id, id=group_id).exists()
		is_group_member = group_models.GroupMembers.objects.filter(group_id=group_id, member_id=user_id).exists()
		return  is_group_owner or is_group_member


class CanInviteMembersToGroup(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.method == 'POST':
			group_id = request.data["group"]
			user_id = request.user.id
			return group_models.Group.objects.filter(pk=group_id, group_owner_id=user_id).exists()
		else:
			return True

class CanAddDeleteGroupPrograms(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.method == 'POST' or request.method == 'DELETE':
			group_id = request.data['group']
			user_id = request.user.id
			return group_models.Group.objects.filter(pk=group_id, group_owner_id=user_id).exists()
		else:
			return True