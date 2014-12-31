# -*- coding: utf-8 -*-
import models
from workout import models as workout_models

class DayProgramViewModel:
    
    def __init__(self, dayProgram, user_profile_id):
        self.day_program = dayProgram
        self.exercise = []
        registers = workout_models.DayRegister.objects.filter(day_program=self.day_program, user_id=user_profile_id).exclude(end_time=None)
        self.is_registered = len(registers) > 0
       
        for ex in models.DayExcersice.objects.filter(day_program=dayProgram):
            self.exercise.append(ShowExersiceViewModel(ex))
        self.number_of_exercises = len(self.exercise)
        
class WeekViewModel:
    
    def __init__(self, week_entity, user_profile_id):
        self.week = week_entity
        self.day_program = []
        for day in models.DayProgram.objects.filter(week=self.week):
            self.day_program.append(DayProgramViewModel(day, user_profile_id))
        
    

class MyProgramsViewModel:
    
    def __init__(self, program_id, user_profile_id):
        self.program = models.Program.objects.get(pk=program_id)
        self.weeks = []
        
        for week in models.Week.objects.filter(program=self.program):
            self.weeks.append(WeekViewModel(week, user_profile_id))
            

class ShowExersiceViewModel:
    
    def __init__(self, exercise_object):
        self.exercise = exercise_object
        self.name = exercise_object.base_excersice.name
        
        
        
    
class ShowDayViewModel:
    
    def __init__(self, day_id):
        self.program = models.DayProgram.objects.get(pk=day_id)
        self.exersices = []
        for exercise in models.DayExcersice.objects.filter(day_program=self.program):
            self.exersices.append(ShowExersiceViewModel(exercise))
        
        
        
        
        
        
        
        
        