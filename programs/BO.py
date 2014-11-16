# -*- coding: utf-8 -*-
from models import Week, Program, DayExcersice, DayProgram

class WeekService:
    repository = Week

    def get_all_from_Program_id(self, id):

        return Week.objects.filter(program_id=id)


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