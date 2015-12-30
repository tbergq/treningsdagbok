import Program.models as program_models
import Workout.models as workout_models
from django.db import models, connection


class LogoutService(models.Manager):

	def logout(self, user_id):
		cursor = connection.cursor()
		cursor.execute("""
			DELETE FROM authtoken_token
			where user_id = %s
			""" % user_id)

		return True