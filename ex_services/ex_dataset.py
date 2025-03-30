import re
from datetime import datetime
from ex_services.ex_data import ExData
from ex_services.ex_metadata import ExMetadata
from ex_services.regex_utils import RegexUtils

class ExDataset:
	def __init__(self):
		self._metadata = ExMetadata()
		self.data = []
		self.stripped = None

	def compile_data(self):
		for x in self.data:
			x.__dict__.update(self._metadata.__dict__)

	def handle_rep_scheme(self):
		ex = ExData(ex=self.stripped, reps=self._metadata.rep_scheme)
		self.data.append(ex)

	def handle_ex_reps_match(self, match):
		if " or " in match.lower():
			split = match.split(" or ")
			for x in split:
				self.data.append(ExData(ex_reps=x, has_alt=True))
			return True
		self.data.append(ExData(ex_reps=match))

	def parse_line(self, line):
		# refactor for a loop of some kind?
		self.stripped = line.strip()

		if not self.stripped:
			return None

		if self._metadata.set(self.stripped):
			return True

		if self._metadata.rep_scheme:
			self.handle_rep_scheme()
			return True

		ex_reps_match = RegexUtils.try_match(self.stripped, "ex_reps")

		if ex_reps_match:
			self.handle_ex_reps_match(ex_reps_match)
		else:
			self._metadata.notes = self.stripped.strip()


		return True
