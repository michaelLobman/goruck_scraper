from ex_services.regex_utils import RegexUtils

class ExData():
	def __init__(self, ex=None, ex_reps=None, has_alt=False):
		self.ex = ex or RegexUtils.try_match(ex_reps, "ex")
		self.reps = None if ex else RegexUtils.try_match(ex_reps, "reps")
		self.has_alt = has_alt