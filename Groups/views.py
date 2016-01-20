from django.shortcuts import render
from rest_framework import generics
import Groups.models as group_models
import Program.models as program_models
import Groups.serializers as group_serializers
import Program.serializers as program_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from Groups.permissions import IsGroupOwner, IsGroupMemberOrOwner, CanInviteMembersToGroup, CanAddDeleteGroupPrograms

# Create your views here.


class GroupsList(generics.ListCreateAPIView):
	serializer_class = group_serializers.GroupSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		include_member_groups = self.request.query_params.get('includeMemberShipGroups', False)
		my_groups = group_models.Group.objects.filter(group_owner_id=self.request.user.id)
		
		if include_member_groups:
			member_group_ids = group_models.GroupMembers.objects.filter(member_id=self.request.user.id).values('group_id')
			member_groups = group_models.Group.objects.filter(id__in=member_group_ids)
			return my_groups | member_groups 

		return my_groups

	def perform_create(self, serializer):
		serializer.save(group_owner=self.request.user)

		
class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class =group_serializers.GroupSerializer
	permission_classes = (IsAuthenticated, IsGroupOwner,)

	def get_queryset(self):
		my_groups = group_models.Group.objects.filter(group_owner_id=self.request.user.id)
		group_ids = group_models.GroupMembers.objects.filter(member_id=self.request.user.id).values('group_id')

		return my_groups | group_models.Group.objects.filter(id__in=group_ids) 


class InviteList(generics.ListCreateAPIView):
	serializer_class = group_serializers.InviteSerializer
	permission_classes = (IsAuthenticated, CanInviteMembersToGroup,)

	def get_queryset(self):
		return group_models.Invite.objects.filter(invited_id=self.request.user.id)

	def create(self, request, *args, **kwargs):
		try:
			return super(InviteList, self).create(request, *args, **kwargs)
		except Exception as e:
			
			return Response({'error' : e.args[0]}, status.HTTP_409_CONFLICT)

	def perform_create(self, serializer):
		invited_id=self.request.data["invited_id"]
		group_id=self.request.data["group"]
		invite = group_models.Invite.objects.filter(invited_id=invited_id, group_id=group_id)
		member = group_models.GroupMembers.objects.filter(group_id=group_id, member_id=invited_id)
		if len(invite) > 0:
			raise Exception('User is already invited')
		if len(member) > 0:
			raise Exception('User is already a member of this group')
		serializer.save(inviter=self.request.user, invited_id=invited_id, group_id=group_id)
		
class InviteDetail(generics.DestroyAPIView):
	serializer_class = group_serializers.InviteSerializer
	permission_classes = (IsAuthenticated, )

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


class AddableProgramsList(generics.ListAPIView):
	serializer_class = program_serializers.ProgramSimpleSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		group_id = self.request.query_params.get('group_id', 0)
		my_group_programs = group_models.GroupPrograms.objects.filter(group_id=group_id).values('program_id')
		except_programs = program_models.Program.objects.filter(id__in=my_group_programs)
		return program_models.Program.objects.filter(user=self.request.user).exclude(id__in=except_programs)



class GroupProgramsList(generics.ListCreateAPIView):
	serializer_class = group_serializers.GroupProgramSerializer
	permission_classes = (IsAuthenticated, CanAddDeleteGroupPrograms,)

	def get_queryset(self):
		group_id = self.request.query_params.get('group_id', 0)
		return group_models.GroupPrograms.objects.filter(group_id=group_id)

	def perform_create(self, serializer):
		serializer.save(program_id=self.request.data['program_id'], group_id=self.request.data['group'])

class GroupProgramDelete(generics.DestroyAPIView):
	serializer_class = group_serializers.GroupProgramSerializer
	permission_classes = (IsAuthenticated, CanAddDeleteGroupPrograms,)

	def get_queryset(self):
		return group_models.GroupPrograms.objects.filter(program__user=self.request.user)



class GroupMessagesList(generics.ListCreateAPIView):
	serializer_class = group_serializers.GroupMessagesSerializer
	permission_classes = (IsAuthenticated, IsGroupMemberOrOwner,)
	queryset = group_models.GroupMessages.objects.all().order_by('-time')

	def perform_create(self, serializer):
		serializer.save(group_id=self.request.query_params.get('groupId', None), user_id=self.request.user.id)


	def get_queryset(self):
		group_id=self.request.query_params.get('groupId', 0)
		return group_models.GroupMessages.objects.filter(group_id=group_id).order_by('-time')








