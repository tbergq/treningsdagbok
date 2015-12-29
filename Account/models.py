from django.contrib.auth.models import User
from django.db import models

#class UserProfile(models.Model):
#	user = models.OneToOneField(User)



class UserReset(models.Model):
	user = models.ForeignKey(User)
	guid = models.CharField(max_length=255)
	reset_time = models.DateTimeField()

class SystemSettings(models.Model):
	key = models.CharField(max_length=255)
	value = models.CharField(max_length=255)
