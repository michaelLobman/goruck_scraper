import re
from datetime import datetime
from csv_services.exercise_data import ExerciseData
from csv_services.regex_utils import RegexUtils

class ExerciseDataset:
	def __init__ (self):
		self._identity_counter = 0
		self._title = None
		self._date = None
		self._rounds = None
		self._rx = None
		self._duration = None
		self.data = []
		self._state_change = False

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		self._state_change = self.set_state_change(value, self._title)
		self._title = value

	@property 
	def date(self):
		return self._date

	@date.setter
	def date(self, value):
		self._state_change = self.set_state_change(value, self._date)
		self._date = value

	@property
	def rounds(self):
		return self._rounds

	@rounds.setter
	def rounds(self, value):
		self._state_change = self.set_state_change(value, self._rounds)
		self._rounds = value

	@property
	def rx(self):
		return self._rx

	@rx.setter
	def rx(self, value):
		self._state_change = self.set_state_change(value, self._rx)
		self._rx = value

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, value):
		self._state_change = self.set_state_change(value, self._duration)
		self._duration= value
	
	@property
	def id_counter(self):
		self._identity_counter += 1
		return self._identity_counter

	@property
	def previous_id(self):
		return self._identity_counter - 1

	def set_state_change(self, old, new):
		return self._state_change or old != new

	def set_metadata(self, line):
		self.date = self.date if self.date else RegexUtils.try_match(line, "date")
		self.title = self.title if self.title else RegexUtils.try_match(line, "title")
		self.rounds = self.rounds if self.rounds else RegexUtils.try_match(line, "rounds")
		self.rx = self.rx if self.rx else RegexUtils.try_match(line, "rx")
		return self._state_change

	def parse_line(self, line):
		self._state_change = False

		if not line.strip():
			return None

		if self.set_metadata(line):
			return True

		ex_reps = RegexUtils.try_match(line, "ex_reps")

		if not ex_reps:
			return False

		if "or" in ex_reps.lower():
			split = ex_reps.split("or")
			for x in split:
				self.data.append(ExerciseData(self, x, True))
			return True

		self.data.append(ExerciseData(self, ex_reps))

		return True


		




