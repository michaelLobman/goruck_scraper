from csv_services.regex_utils import RegexUtils

class ExerciseData():
	def __init__(self, dataset, ex_reps, has_alt = False):
		self.id = dataset.id_counter
		self.date = dataset.date
		self.rx = dataset.rx
		self.rounds = dataset.rounds
		self.duration = dataset.duration
		self.ex = RegexUtils.try_match(ex_reps, "ex")
		self.reps = RegexUtils.try_match(ex_reps, "reps")
		self.has_alt = has_alt