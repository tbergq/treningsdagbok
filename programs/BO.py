# -*- coding: utf-8 -*-
from models import Week, Program, DayExcersice, DayProgram
from django.db import models

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
        


class ProgramService:
    
    def __init__(self, program_id):
        self.program = Program.objects.get(pk=program_id)
        self.weeks = self.get_weeks()
        
        
    def get_weeks(self):
        return Week.objects.filter(program=self.program)
        
        
    
    
    
    
class DayProgramService:
    
    def get_from_day_exercise_id(self, day_id):
        day_exercise = DayExcersice.objects.get(pk=day_id)
        day_program = DayProgram.objects.get(pk=day_exercise.day_program.id)
        print "day program_id: %s" % day_program.id
        return day_program
    
class BaseExerciseService(models.Manager):
    
    def get_distinct_muscle_groups(self):
        from django.db import connection
        muscle_groups = []
        cursor = connection.cursor()
        cursor.execute("""
            SELECT distinct muscle_group FROM Treningsdagbok.programs_baseexercise""")
        for name in cursor.fetchall():
            muscle_groups.append(name)
        return muscle_groups
    
    
    