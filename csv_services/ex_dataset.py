import re
from datetime import datetime
from csv_services.ex_data import ExData
from csv_services.ex_metadata import ExMetadata
from csv_services.regex_utils import RegexUtils

class ExDataset:
	def __init__ (self):
		self._id_incrementer = 0
		# metadata property
		self._metadata = ExMetadata()
		self.data = []

	@property
	def id_incrementer(self):
		self._id_incrementer += 1
		return self._id_incrementer
	
	def parse_line(self, line):
		if not line.strip():
			return None

		if self._metadata.set_metadata(line):
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


		




