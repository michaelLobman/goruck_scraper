import re
from datetime import datetime

class RegexUtils():
	DATE = r"^\d{1,2}\.\d{1,2}\.\d{1,2}"
	TITLE = r"“(.*?)”"
	ROUNDS = r"(\d+)\s+rounds"
	EX_REPS = r"^\d.*"
	EX = r"\s.*"
	REPS = r"^\d\S*"
	RX = r"^(Rx:|Male:).*"

	@staticmethod
	def match_date(line):
		match = re.search(RegexUtils.DATE, line)
		if not match:
			return None
		date_str = match.group()
		return datetime.strptime(date_str, "%m.%d.%y")

	@staticmethod
	def match_title(line):
		match = re.search(RegexUtils.TITLE, line)
		if not match:
			return None
		return match.group()

	@staticmethod
	def match_rounds(line):
		match = re.search(RegexUtils.ROUNDS, line.lower())
		if not match:
			return None
		return match.group(1)

	@staticmethod
	def match_ex_reps(line):
		match = re.search(RegexUtils.EX_REPS, line)
		if not match:
			return None
		return match.group()

	@staticmethod
	def match_ex(line):
		match = re.search(RegexUtils.EX, line.strip())
		if not match:
			return None
		return match.group()

	@staticmethod
	def match_reps(line):
		match = re.search(RegexUtils.REPS, line.strip())
		if not match:
			return None
		return match.group()


