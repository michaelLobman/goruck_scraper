import re
from datetime import datetime

class RegexUtils():
	DATE = r"^\d{1,2}\.\d{1,2}\.\d{1,2}"
	TITLE = r"“(.*?)”"
	ROUNDS = r"(\d+)\s+rounds"
	EX_REPS = r"^\d+\s[A-Za-z-\s\d]+"
	EX = r"\s[A-Za-z-\s]+"
	REPS = r"^\d+[A-Za-z-\d]+"

	@staticmethod
	def match_date(self,line):
		match = re.search(self._date_pattern, line)
		if not match:
			return None
		date_str = match.group()
		return datetime.strptime(date_str, "%m.%d.%y")

	@staticmethod
	def match_title(self,line):
		match = re.search(self._title_pattern, line)
		if not match:
			return None
		return match.group()

	@staticmethod
	def match_rounds(self,line):
		match = re.search(self._rounds_pattern, line.lower())
		if not match:
			return None
		return match.group(1)

	@staticmethod
	def match_exercise_and_reps(self, line):
		match = re.search(self._exercise_and_reps_pattern, line)
		if not match:
			return None
		return match.group()

	@staticmethod
	def match_exercise(self, line):
		match = re.search(self._exercise_pattern, line.strip())
		if not match:
			return None
		return match.group()
		
	@staticmethod
	def match_reps(self, line):
		match = re.search(self._reps_pattern, line.strip())
		if not match:
			return None
		return match.group()


