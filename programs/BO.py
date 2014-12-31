# -*- coding: utf-8 -*-
from models import Week, Program, DayExcersice, DayProgram, BaseExercise
from django.db import models
import forms
from __builtin__ import True
from workout import models as workout_models
from group import models as group_models
from django.db import connection

class WeekService:
    repository = Week

    def get_all_from_Program_id(self, id):
        return Week.objects.filter(program_id=id)
    
    def copy_week_from_week_id(self, id):
        original_week = Week.objects.get(pk=id)
        original_program = original_week.program
        new_week_name = 'Uke %d' % (len(Week.objects.filter(program=original_program)) + 1)
        new_week = Week(name=new_week_name,program=original_program)
        new_week.save()
        existing_days = DayProgram.objects.filter(week=original_week)
        day_number = 1
        for existing_day in existing_days:
            new_day_name = 'Dag %d' % day_number
            day_number += 1
            new_day = DayProgram(name=new_day_name, week=new_week)
            new_day.save()
            existing_exercises = DayExcersice.objects.filter(day_program=existing_day)
            for existing_exercise in existing_exercises:
                new_exercise = DayExcersice()
                new_exercise.base_excersice = existing_exercise.base_excersice
                new_exercise.set = existing_exercise.set
                new_exercise.reps = existing_exercise.reps
                new_exercise.day_program = new_day
                new_exercise.description = existing_exercise.description
                new_exercise.break_time = existing_exercise.break_time
                new_exercise.save()
    
    def rename_weeks(self, programId):
        weeks = self.get_all_from_Program_id(programId)
        count = 1
        for rename_week in weeks:
            rename_week.name = 'Uke %d' % count
            count += 1
            rename_week.save()
        
    def is_deletable(self,weekId):
        is_deletable = True
        days = DayProgram.objects.filter(week_id=weekId)
        for day in days:
            if len(workout_models.DayRegister.objects.filter(day_program=day)) > 0:
                is_deletable = False
        return is_deletable

class ProgramService:
    
   # def __init__(self, program_id):
    #    self.program = Program.objects.get(pk=program_id)
     #   self.weeks = self.get_weeks()
        
        
    def get_weeks(self, id):
        return Week.objects.filter(program_id=id)
        
    def is_deletable(self, programId):
        is_deletable = True
        week_service = WeekService()
        my_weeks = self.get_weeks(programId)
        for week in my_weeks:
            week_is_deletable = week_service.is_deletable(week.id)            
            if not week_is_deletable:
                return False
        return is_deletable
    
    def get_group_programs(self, user_profile):
        groups = group_models.GroupMembers.objects.filter(member=user_profile)
        programs = []
        for group in groups:
            program_list = group_models.GroupPrograms.objects.filter(group_id=group.group_id)
            programs.extend(program_list)
        return programs
            
    
    
    
class DayProgramService:
    
    def get_from_day_exercise_id(self, day_id):
        day_exercise = DayExcersice.objects.get(pk=day_id)
        day_program = DayProgram.objects.get(pk=day_exercise.day_program.id)
        
        return day_program
    
class ProgramManager(models.Manager):
        
        def get_programs_for_register(self, user_profile_id):
            cursor = connection.cursor()
            cursor.execute("""
            Select * from Treningsdagbok.programs_program
            where user_id = %s
            UNION
            SELECT * FROM Treningsdagbok.programs_program
            where id in
            (SELECT program_id from Treningsdagbok.group_groupprograms
            where group_id in
            (select group_id from Treningsdagbok.group_groupmembers
            where member_id = %s))
            order by date desc""" %(user_profile_id, user_profile_id))
            result_list = []
            for row in cursor.fetchall():
                element = Program(id=row[0],name=row[1],date=row[2],user_id=row[3])
                result_list.append(element)
            return result_list
    
class BaseExerciseService(models.Manager):
    
    def get_distinct_muscle_groups(self):
        #from django.db import connection
        muscle_groups = []
        cursor = connection.cursor()
        cursor.execute("""
            SELECT distinct muscle_group FROM Treningsdagbok.programs_baseexercise""")
        for name in cursor.fetchall():
            muscle_groups.append(name)
        return muscle_groups
    
    def get_all(self):
        exercises = BaseExercise.objects.all().order_by('muscle_group')
        exercise_list = [{'name' : "--Velg--", 'value' : None}]
        for element in exercises:
            name = u"%s - %s" % (element.muscle_group, element.name)
            exercise_list.append({'name' : name, 'value' : element.id})
            
        return exercise_list
    
    
class DayExerciseService:
    
    def setup_dayExerciseForm(self, request, number):
        
        form = forms.DayExerciseForm()
        form.day_program = request.POST.get('day_program')
        form.base_excersice = request.POST.get('[%s].exercise' % number, None)
        form.set = request.POST.get('[%s].set' % number, None)
        form.reps = request.POST.get('[%s].reps' % number,None)
        form.description = request.POST.get('[%s].description' % number, '')
        form.break_time = request.POST.get('[%s].break_time' % number, None)
        
        return form

    def is_deletable(self, dayExerciseId):
        return len(workout_models.DayRegister.objects.filter(day_program_id=dayExerciseId)) > 0




    
    