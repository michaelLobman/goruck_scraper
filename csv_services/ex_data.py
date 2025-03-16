from csv_services.regex_utils import RegexUtils

class ExData():
	def __init__(self, ex_reps, has_alt=False):
		self.ex = RegexUtils.try_match(ex_reps, "ex")
		self.reps = RegexUtils.try_match(ex_reps, "reps")
		self.has_alt = has_alt