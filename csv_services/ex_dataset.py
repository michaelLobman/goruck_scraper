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
		# TODO: refactor each into own method?

		stripped = line.strip()

		if not stripped:
			return None

		if self._metadata.set(stripped):
			return True

		if self._metadata.rep_scheme:
			ex = ExData(ex=stripped, reps=self._metadata.rep_scheme)
			self.data.append(ex)
			return True

		ex_match = RegexUtils.try_match(stripped, "ex_reps")

		if not ex_match:
			self._metadata.notes = stripped.strip()
			return True

		if " or " in ex_match.lower():
			split = ex_match.split(" or ")
			for x in split:
				self.data.append(ExData(ex_reps=x, has_alt=True))
			return True

		self.data.append(ExData(ex_reps=ex_match))

		return True
