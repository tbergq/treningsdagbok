from django.shortcuts import render
from rest_framework import generics
import Groups.models as group_models
import Groups.serializers as group_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


class GroupsList(generics.ListCreateAPIView):
	serializer_class = group_serializers.GroupSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return group_models.Group.objects.filter(group_owner_id=self.request.user.id)

	def perform_create(self, serializer):
		serializer.save(group_owner=self.request.user)

		
class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class =group_serializers.GroupSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return group_models.Group.objects.filter(group_owner_id=self.request.user.id)


class InviteList(generics.ListCreateAPIView):
	serializer_class = group_serializers.InviteSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return group_models.Invite.objects.filter(invited_id=self.request.user.id)

	def perform_create(self, serializer):
		serializer.save(inviter=self.request.user, invited_id=self.request.data["invited_id"], group_id=self.request.data["group"])
		
class InviteDetail(generics.DestroyAPIView):
	serializer_class = group_serializers.InviteSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return group_models.Invite.objects.filter(invited_id=self.request.user.id)



	def delete(self, request, pk=None):
		accepted = request.query_params.get('accepted', False)
		invite = group_models.Invite.objects.get(pk=pk)
		if accepted:
			group_member = group_models.GroupMembers(group_id=invite.group_id, member_id=invite.invited_id)
			group_member.save()
			
		
		invite.delete()
		return Response({}, status.HTTP_200_OK)
			

class GroupMembersList(generics.ListCreateAPIView):
	serializer_class = group_serializers.GroupMemberSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		group_id = self.request.query_params.get('group_id', 0)
		return group_models.GroupMembers.objects.filter(group_id=group_id)




