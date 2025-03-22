from csv_services.regex_utils import RegexUtils

class ExMetadata():
	def __init__(self):
		self.title = None
		self.date = None
		self.rounds = None
		self.rx = None
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
				# if match and attr == "scoring":
					# THIS IS A NEW EX INSTANCE for the alst one
					# bc the "notes" in the final ex don't match anything at all...
					# import pdb; pdb.set_trace()  # Breakpoint here
				if attr != "title":
					return True
		return False