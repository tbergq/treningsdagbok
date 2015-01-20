# -*- coding: utf-8 -*-
'''
Created on 13. nov. 2014

@author: tronbe
'''
from models import DayRegister, ExcerciseRegister
from programs import models as program_models
from account import models as account_models
from django.db import models, connection

class ExerciseRegisterService:
    
    def get_set_number(self, ids):
        return 1
    
    
    
class SelectListItem():
    
    def __init__(self, name, value, is_selected):
        self.name = name
        self.value = value
        self.is_selected = is_selected
        
    
class WorkoutManager(models.Manager):
    def get_day_registers_for_program(self, requested_program_id):
        cursor = connection.cursor()
        cursor.execute("""
        select * from workout_dayregister
        where end_time is not null and day_program_id in(
        select id from programs_dayprogram
        where week_id in(
        select id from programs_week 
        where program_id = %s)) order by start_time desc
                       """ % requested_program_id)
        result_list = []
        for row in cursor.fetchall():
            
            day_register = DayRegister(id=row[0], day_program_id=row[3], user_id=row[4], start_time=row[1], end_time=row[2])
            result_list.append(day_register)
        return result_list
    
    def get_selectlistitems_for_registered_workout(self, user_id, requested_id):
        cursor = connection.cursor()
        cursor.execute("""
        select name, id from programs_program
        where id in(
        select program_id from programs_week
        where id in(
        select week_id from programs_dayprogram
        where id in(
        select day_program_id from workout_dayregister
        where end_time is not null 
        and user_id = %s
        )
        )
        ) 
                       """% user_id)
        result_list = []
        for row in cursor.fetchall():
            is_requested = int(row[1]) == int(requested_id)
            select_list_item = SelectListItem(row[0],row[1], is_requested)
            result_list.append(select_list_item)
        return result_list