import Program.models as program_models
import Workout.models as workout_models


class SelectDayService():

	def get_data(self, program_id):
		print "get data"
		print program_id
		program = program_models.Program.objects.get(pk=program_id)
		program.weeks = program_models.Week.objects.filter(program_id=program_id)
		print "start looping"
		print program.weeks
		for week in program.weeks:
			week.days = program_models.Day.objects.filter(week=week)

			for day in week.days:
				register_day = workout_models.DayRegister.objects.get(day_program=day.id)

				if register_day != None:
					day.disabled = register_day.end_time != None
				else:
					day.disabled = False

		return program


