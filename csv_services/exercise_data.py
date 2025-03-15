from csv_services.regex_utils import RegexUtils

class ExerciseData():
	def __init__(self, dataset, exercise_and_reps):
		# perhaps exercise data doesn't need all the other info?
		self.id = dataset.id_counter
		self.date = dataset.date
		self.rx = dataset.rx
		self.rounds = dataset.rounds
		self.duration = dataset.duration
		# TODO: refactor
		self.regex = RegexUtils()
		self.exercise = self.regex.match_exercise(exercise_and_reps)
		self.reps = self.regex.match_reps(exercise_and_reps)
		self.primary_ex_key = None