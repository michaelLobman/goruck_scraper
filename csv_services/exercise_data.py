from csv_services.regex_utils import RegexUtils

class ExerciseData():
	def __init__(self, dataset, ex_reps, has_alt = False):
		self.id = dataset.id_counter
		self.date = dataset.date
		self.rx = dataset.rx
		self.rounds = dataset.rounds
		self.duration = dataset.duration
		# TODO: refactor
		self.ex = RegexUtils.match_ex(ex_reps)
		self.reps = RegexUtils.match_reps(ex_reps)
		self.has_alt = has_alt