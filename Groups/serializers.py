from rest_framework import serializers
import Groups.models as group_models
import Account.serializers as account_serializers
import Program.serializers as program_serializers
from rest_framework.validators import UniqueTogetherValidator

class GroupSerializer(serializers.ModelSerializer):
	#group_owner = serializers.ReadOnlyField(source="user.id")
	group_owner = account_serializers.UserInfoSerializer(many=False, read_only=True)
	class Meta:
		model = group_models.Group
		fields = '__all__'
		

class InviteSerializer(serializers.ModelSerializer):
	invited = account_serializers.UserInfoSerializer(many=False, read_only=True)
	inviter = account_serializers.UserInfoSerializer(many=False, read_only=True)
	group = GroupSerializer(many=False, read_only=True)

	class Meta:
		model = group_models.Invite
		fields = '__all__'
		"""validators = [
			UniqueTogetherValidator(
				queryset=group_models.Invite.objects.all(),
				fields=('invited', 'group')
			)
		]"""

class GroupMemberSerializer(serializers.ModelSerializer):
	member = account_serializers.UserInfoSerializer(many=False, read_only=True)
	class Meta:
		model = group_models.GroupMembers
		fields = '__all__'

class GroupProgramSerializer(serializers.ModelSerializer):
	#program = program_serializers.ProgramSimpleSerializer(many=False, read_only=True)
	class Meta:
		model = group_models.GroupPrograms
		fields = '__all__'
		depth = 1

class GroupMessagesSerializer(serializers.ModelSerializer):
	user = account_serializers.UserInfoSerializer(many=False, read_only=True)
	class Meta:
		model = group_models.GroupMessages
		fields = '__all__'
		depth = 1