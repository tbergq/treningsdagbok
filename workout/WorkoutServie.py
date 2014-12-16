# -*- coding: utf-8 -*-
'''
Created on 13. nov. 2014

@author: tronbe
'''
from models import DayRegister, ExcerciseRegister
from programs import models as program_models
from account import models as account_models

class ExerciseRegisterService:
    
    
    
    def get_set_number(self, ids):
        return 1
    
    
    def get_name(self, reg_id):
        day_register_object = DayRegister.objects.get(pk=reg_id)
        day_program_object = program_models.DayProgram.objects.get(pk=day_register_object.day_program_id)
        week_object = program_models.Week.objects.get(pk=day_program_object.week_id)
        program_object = program_models.Program.objects.get(pk=week_object.program_id)
        return "%s - %s/%s" % (program_object.name, week_object.name, day_program_object.name) 
    
    