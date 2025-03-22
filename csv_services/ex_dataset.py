import re
from datetime import datetime
from csv_services.ex_data import ExData
from csv_services.ex_metadata import ExMetadata
from csv_services.regex_utils import RegexUtils
# need to check metadata the compilation
class ExDataset:
	def __init__(self):
		self._metadata = ExMetadata()
		self.data = []

	def compile_data(self):
		for x in self.data:
			x.__dict__.update(self._metadata.__dict__)

	def parse_line(self, line):
		if not line.strip():
			return None

		if self._metadata.set(line):
			return True

		ex_reps = RegexUtils.try_match(line, "ex_reps")

		if not ex_reps:
			self._metadata.notes = line.strip()
			return True

		if "or" in ex_reps.lower():
			split = ex_reps.split("or")
			for x in split:
				self.data.append(ExData(x, True))
			return True

		self.data.append(ExData(ex_reps))

		return True
