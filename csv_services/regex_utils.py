import re
from datetime import datetime

class RegexUtils():
	# refactor to be more abstract
	def __init__(self):
		self._date_pattern = r"^\d{1,2}\.\d{1,2}\.\d{1,2}"
		self._title_pattern = r"“(.*?)”"
		self._rounds_pattern = r"(\d+)\s+rounds"

	def match_date(self,line):
		match = re.search(self._date_pattern, line)
		if not match:
			return False
		date_str = match.group()
		return datetime.strptime(date_str, "%m.%d.%y")

	def match_title(self,line):
		match = re.search(self._title_pattern, line)
		if not match:
			return False
		return match.group()

	def match_rounds(self,line):
		match = re.search(self._rounds_pattern, line.lower())
		if not match:
			return None
		return match.group()

