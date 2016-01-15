import Program.models as program_models
import Workout.models as workout_models
from django.db import models, connection

class SelectDayService():

	def get_data(self, program_id):
		program = program_models.Program.objects.get(pk=program_id)
		program.weeks = program_models.Week.objects.filter(program_id=program_id)

		for week in program.weeks:
			week.days = program_models.Day.objects.filter(week=week)

			for day in week.days:
				register_day = workout_models.DayRegister.objects.get(day_program=day.id)

				if register_day != None:
					day.disabled = register_day.end_time != None
				else:
					day.disabled = False

		return program

class OneRepMaxManager(models.Manager):
	
	def get_distinct(self, user_id, table_name):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT distinct %s
			from Workout_onerepmax
			where user_id = %s
		""" % (table_name, user_id))
		result=cursor.fetchall()
		return result

class WorkoutManager(models.Manager):

	def get_latest_registers(self, user_id, day_register_id, base_exercise_id):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT * FROM Workout_excerciseregister
			where day_register_id in(
			select id from Workout_dayregister
			where user_id = %s
			and id != %s
			and end_time is not null)
			and day_excersice_id in(
			select id from Program_exercise
			where base_exercise_id = %s
			and day_id in(
			select id from Program_day
			where week_id in(
			select id from Program_week
			where  program_id in(
			select id from Program_program
			where user_id = %s))))
			""" % (user_id, day_register_id, base_exercise_id, user_id))

		result_list = []
		return_list = []
		max_date = None

		for row in cursor.fetchall():
			register = workout_models.ExcerciseRegister(id=row[0], set_number=row[1], reps=row[2], weight=row[3], note=row[4], day_excersice_id=row[5], day_register_id=row[6])
			result_list.append(register)

		for item in result_list:
			if max_date == None or item.day_register.start_time > max_date:
				max_date = item.day_register.start_time

		for item in result_list:
			if item.day_register.start_time == max_date:
				return_list.append(item)
		
		return return_list

	def get_latest_by_user_id(self, user_id):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT * FROM Workout_excerciseregister
			where day_register_id in(
			select id from Workout_dayregister
			where user_id = %s)
			""" % user_id)

		result_list = []
		for row in cursor.fetchall():
			register = workout_models.ExcerciseRegister(id=row[0], set_number=row[1], reps=row[2], weight=row[3], note=row[4], day_excersice_id=row[5], day_register_id=row[6])
			result_list.append(register)
		return result_list

	def get_day_registers_from_program_id(self, program_id, user_id):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT * FROM Workout_dayregister
			where user_id = %s
			and day_program_id in(
			select id from Program_day
			where week_id in(
			select id from Program_week
			where program_id = %s)
			)
			""" % (user_id, program_id))

		result_list = []
		for row in cursor.fetchall():
			result = workout_models.DayRegister(id=row[0], start_time=row[1], end_time=row[2], day_program_id=row[3], user_id=row[4])
			result_list.append(result)
		return result_list



class OneRepMaxService():

	def get_latest(self, user_id):
		latest = []
		ids = OneRepMaxManager().get_distinct(user_id, 'base_exercise_id')
		
		for id in ids:
			rm = workout_models.OneRepMax.objects.filter(base_exercise_id=id).order_by('-date')[0]
			latest.append(rm)

		return latest








