import re
from datetime import datetime
from csv_services.exercise_data import ExerciseData
from csv_services.regex_utils import RegexUtils

class ExerciseDataset:
	def __init__ (self, title=None, date=None, rounds=None, rx=None, duration=None):
		self._identity_counter = 0
		self.title = title
		self.date = date
		self.rounds = rounds
		self.rx = rx
		self.duration = duration
		self.regex = RegexUtils()
		self.dataset = []

	@property
	def id_counter(self):
		self._identity_counter += 1
		return self._identity_counter
		
	def parse_line(self, line):
		stripped = line.strip()
		if not stripped:
			return None

		date_match = self.regex.match_date(line)
		title_match = self.regex.match_title(line)

		if date_match and title_match:
			self.date = date_match
			self.title = title_match
			print(self.date)
			print(self.title)

		




