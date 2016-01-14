# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from Program.models import Program

class Group(models.Model):
	name = models.CharField(max_length=128)
	group_owner = models.ForeignKey(User)
	created_date = models.DateTimeField()
    
    
class GroupMembers(models.Model):
	group = models.ForeignKey(Group)
	member = models.ForeignKey(User)
	class Meta:
		unique_together = (("group", "member"),)
    
class GroupPrograms(models.Model):
	program = models.ForeignKey(Program)
	group = models.ForeignKey(Group)


class Invite(models.Model):
	invited = models.ForeignKey(User, related_name='invited')
	inviter = models.ForeignKey(User, related_name='inviter')
	group = models.ForeignKey(Group)
	class Meta:
		unique_together = (("group", "invited"),)