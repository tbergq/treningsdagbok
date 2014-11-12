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
    
    def __str__(self):
        return "%s - %s" % (self.muscle_group, self.name)

    class Meta:
        unique_together = ('name', 'user',)

class Week(models.Model):
    name = models.CharField(max_length=128)
    program = models.ForeignKey(Program)

class DayProgram(models.Model):
    name = models.CharField(max_length=128)
    week = models.ForeignKey(Week)

class DayExcersice(models.Model):
    base_excersice = models.ForeignKey(BaseExercise)
    set = models.CharField(max_length=10)
    reps = models.CharField(max_length=128)
    day_program = models.ForeignKey(DayProgram)










