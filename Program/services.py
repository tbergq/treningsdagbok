from Program import models as program_models

class ProgramService():

	def get_program(self, program_id):
		program = program_models.Program.objects.get(pk=program_id)
		program.weeks = WeekService.get_weeks(program_id)
		return program


class WeekService():

	def get_weeks(self, program_id):
		weeks = program_models.Week.objects.filter(program_id=program_id)
		return weeks
