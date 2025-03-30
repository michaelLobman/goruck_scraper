from ex_services.regex_utils import RegexUtils

class ExMetadata():
	def __init__(self):
		self.title = None
		self.date = None
		self.rounds = None
		self.amrap = None
		self.rep_scheme = None
		self.rx = None
		self.rx_plus = None
		self.male = None
		self.female = None
		self.scoring = None
		self.notes = None

	def set(self, line):
		any_match = False
		for attr, value in vars(self).items():
			if value or attr == "notes":					
				continue
			match = RegexUtils.try_match(line, attr)
			if match:
				setattr(self, attr, match)
				if attr != "title":
					return True
		return False