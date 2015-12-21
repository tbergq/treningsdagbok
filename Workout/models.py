# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

import Program.models as program_models

# Create your models here.

class DayRegister(models.Model):
    day_program = models.ForeignKey(program_models.Day)
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    
    

    

class ExcerciseRegister(models.Model):
    day_excersice = models.ForeignKey(program_models.Exercise)
    day_register = models.ForeignKey(DayRegister)
    set_number = models.IntegerField()
    reps = models.IntegerField()
    weight = models.TextField(max_length=128)
    note = models.TextField(max_length=128, blank=True)


class OtherActivity(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    duration = models.IntegerField()
    activity = models.TextField(max_length=128)
    description = models.TextField(blank=True)