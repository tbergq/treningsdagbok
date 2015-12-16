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

	def copy_week_from_week_id(self, id):
		original_week = program_models.Week.objects.get(pk=id)
		original_program = original_week.program
		new_week_name = 'Week %d' % (len(program_models.Week.objects.filter(program=original_program)) + 1)
		new_week = program_models.Week(name=new_week_name,program=original_program)
		new_week.save()
		existing_days = program_models.Day.objects.filter(week=original_week)
		day_number = 1
		for existing_day in existing_days:
			new_day_name = 'Day %d' % day_number
			day_number += 1
			new_day = program_models.Day(name=new_day_name, week=new_week)
			new_day.save()
			existing_exercises = program_models.Exercise.objects.filter(day=existing_day)
			for existing_exercise in existing_exercises:
				new_exercise = program_models.Exercise()
				new_exercise.base_exercise = existing_exercise.base_exercise
				new_exercise.set = existing_exercise.set
				new_exercise.reps = existing_exercise.reps
				new_exercise.day = new_day
				new_exercise.description = existing_exercise.description
				new_exercise.break_time = existing_exercise.break_time
				new_exercise.save()
		return new_week.id