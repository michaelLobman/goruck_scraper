import re
from datetime import datetime
from csv_services.ex_data import ExData
from csv_services.ex_metadata import ExMetadata
from csv_services.regex_utils import RegexUtils

class ExDataset:
	def __init__(self, seed=-1):
		self._id_incrementer = seed
		self._metadata = ExMetadata()
		self.data = []

	def compile_data(self):
		max_id = 0
		for x in self.data:
			max_id = max(x.id, max_id)
			x.__dict__.update(self._metadata.__dict__)
		return max_id

	@property
	def id_incrementer(self):
		self._id_incrementer += 1
		return self._id_incrementer
	
	def parse_line(self, line):
		if not line.strip():
			return None

		if self._metadata.set(line):
			return True

		ex_reps = RegexUtils.try_match(line, "ex_reps")

		if not ex_reps:
			return False

		if "or" in ex_reps.lower():
			split = ex_reps.split("or")
			for x in split:
				self.data.append(ExData(self.id_incrementer, x, True))
			return True

		self.data.append(ExData(self.id_incrementer, ex_reps))

		return True


		




