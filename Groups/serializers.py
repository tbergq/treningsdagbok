from rest_framework import serializers
import Groups.models as group_models
import Account.serializers as account_serializers

class GroupSerializer(serializers.ModelSerializer):
	group_owner = serializers.ReadOnlyField(source="user.id")
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

class GroupMemberSerializer(serializers.ModelSerializer):
	member = account_serializers.UserInfoSerializer(many=False, read_only=True)
	class Meta:
		model = group_models.GroupMembers
		fields = '__all__'