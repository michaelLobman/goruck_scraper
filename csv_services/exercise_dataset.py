import re
from datetime import datetime
from csv_services.exercise_data import ExerciseData

class ExerciseDataset:
	def __init__ (self, title=None, date=None, rounds=None, rx=None, duration=None):
		self._identity_counter = 0
		self.title = title
		self.date = date
		self.rounds = rounds
		self.rx = rx
		self.duration = duration
		self.dataset = []
		self._date_pattern = r"^\d{1,2}\.\d{1,2}\.\d{1,2}"
		self._title_pattern = r"“(.*?)”"

	@property
	def id_counter(self):
		self._identity_counter += 1
		return self._identity_counter
		
	def parse_line(self, line):
		stripped = line.strip()
		if not stripped:
			return None
		date_match = self.get_date_match(line)
		title_match = self.get_title_match(line)

		# do these even need to be stored on class or just child?
		if date_match and title_match:
			self.date = date_match
			self.title = title_match
			print(self.date)
			print(self.title)

		
	def get_date_match(self,line):
		match = re.search(self._date_pattern, line)
		if not match:
			return False
		date_str = match.group()
		return datetime.strptime(date_str, "%m.%d.%y")

	def get_title_match(self,line):
		match = re.search(self._title_pattern, line)
		if not match:
			return False
		return match.group()


