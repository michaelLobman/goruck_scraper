from csv_services.regex_utils import RegexUtils

class ExMetadata():
	def __init__(self):
		self.title = None
		self.date = None
		self.rounds = None
		self.rx = None

	def set(self, line):
		any_match = False
		for attr, value in vars(self).items():
			if value:					
				continue
			match = RegexUtils.try_match(line, attr)
			if match:
				setattr(self, attr, match)
				if attr != "title":
					return True
		return False