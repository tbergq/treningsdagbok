# -*- coding: utf-8 -*-
from django.db import models
from account.models import UserProfile

class Program(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
    user = models.ForeignKey(UserProfile)
    
    

class BaseExercise(models.Model):
    muscle_group = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(UserProfile)
    
    def __unicode__(self):
        return "%s - %s" % (self.muscle_group ,self.name)
    
    class Meta:
        unique_together = ('name', 'muscle_group',)

class Week(models.Model):
    name = models.CharField(max_length=128)
    program = models.ForeignKey(Program)

class DayProgram(models.Model):
    name = models.CharField(max_length=128)
    week = models.ForeignKey(Week)
    
    def __unicode__(self):
        return self.name

class DayExcersice(models.Model):
    base_excersice = models.ForeignKey(BaseExercise)
    set = models.CharField(max_length=10)
    reps = models.CharField(max_length=128)
    day_program = models.ForeignKey(DayProgram)
    description = models.CharField(max_length=128, null=True, blank=True)
    break_time = models.TextField(max_length=10,default="2")

    def __unicode__(self):
        return self.base_excersice.name








