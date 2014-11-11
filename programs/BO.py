# -*- coding: utf-8 -*-
from models import Week, Program

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
        
        
        
    