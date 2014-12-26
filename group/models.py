# -*- coding: utf-8 -*-
from django.db import models
from account.models import UserProfile

class Group(models.Model):
    name = models.CharField(max_length=128)
    group_admin = models.ForeignKey(UserProfile)
    max_members = models.IntegerField()
    valid_to_date = models.DateField()
    
    
class GroupMembers(models.Model):
    group = models.ForeignKey(Group)
    member = models.ForeignKey(UserProfile)

