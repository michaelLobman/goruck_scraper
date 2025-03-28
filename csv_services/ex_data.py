from csv_services.regex_utils import RegexUtils

class ExData():
	def __init__(self, ex=None, reps=None, ex_reps=None, has_alt=False):
		self.ex = ex if ex else RegexUtils.try_match(ex_reps, "ex")
		self.reps = reps if reps else RegexUtils.try_match(ex_reps, "reps")
		self.has_alt = has_alt