# -*- coding: utf-8 -*-
from programs import models as program_models
from workout import models as workout_models


        
class DTODayExcercise():
    
    def __init__(self, exercise_id):
        exersice = program_models.DayExcersice.objects.get(pk = exercise_id)
        self.id = exercise_id
        self.name = exersice.base_excersice.name
        self.sets  = exersice.set
        self.reps = exersice.reps
        self.description = exersice.description

class DTODayProgram():
    
    def __init__(self, program_id):
        program = program_models.DayProgram.objects.get(pk=program_id)
        self.id = program.id
        self.name = program.name
        self.exercises = self.get_my_exercises(program)
        
        
    def get_my_exercises(self, program):
        exercises = program_models.DayExcersice.objects.filter(day_program=program)
        dto_exersices = []
        for element in exercises:
            dto_exersices.append(DTODayExcercise(element.id))
        return dto_exersices
        
        