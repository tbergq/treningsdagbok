from django.db import models
#from Account.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.
class BaseExercise(models.Model):
    muscle_group = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    youtube_link = models.CharField(max_length=128, blank=True)
    muscle_group = models.ForeignKey('MuscleGroup')
    description = models.CharField(max_length=128, blank=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.muscle_group ,self.name)
    
    class Meta:
        unique_together = ('name', 'muscle_group',)


class MuscleGroup(models.Model):
	name = models.CharField(max_length=128)

class Program(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField()
    user = models.ForeignKey(User, related_name='program')


class Week(models.Model):
    name = models.CharField(max_length=128)
    program = models.ForeignKey(Program, related_name='weeks')


class Day(models.Model):
    name = models.CharField(max_length=128)
    week = models.ForeignKey(Week, related_name='days')

class Exercise(models.Model):
    base_exercise = models.ForeignKey(BaseExercise, related_name="base_exercises")
    set = models.CharField(max_length=10)
    reps = models.CharField(max_length=128)
    day = models.ForeignKey(Day, related_name='exercises')
    description = models.CharField(max_length=128, null=True, blank=True)
    break_time = models.TextField(max_length=10,blank=True)








