from csv_services.regex_utils import RegexUtils

class ExMetadata():
	def __init__(self):
		self.title = None
		self.date = None
		self.rounds = None
		self.rx = None

	def set_metadata(self, line):
		for attr, value in vars(self).items():
			if value:
				continue
			attr_str = str(attr)
			attr = RegexUtils.try_match(line, attr_str)
			if attr:
				return True
		return False