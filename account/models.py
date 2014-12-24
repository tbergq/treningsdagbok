from django.contrib.auth.models import User
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.ForeignKey(UserType,default=1)

    def __unicode__(self):
        return self.user.username

    def is_regular(self):
        return self.user_type.name == "Regular"
    
    def is_group_member(self):
        return self.user_type.name == "GroupMember"
    
    def is_group_admin(self):
        return self.user_type.name == "GroupAdmin"