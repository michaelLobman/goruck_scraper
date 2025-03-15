import re
from datetime import datetime

class RegexUtils():

	PATTERNS = {
		"date": r"^\d{1,2}\.\d{1,2}\.\d{1,2}",
		"title": r"“(.*?)”",
		"rounds": r"(\d+)\s+rounds",
		"ex_reps": r"^\d.*",
		"ex": r"\s.*",
		"reps": r"^\d\S*",
		"rx": r"^(rx:|male:).*"
	}

	@staticmethod
	def try_match(line, key):
		pattern = RegexUtils.PATTERNS[key]
		match = re.search(pattern, line.lower())
		if not match:
			return None
		output = match.group()
		if key == "rounds":
			output = match.group(1)
		elif key == "date":
			output = datetime.strptime(output, "%m.%d.%y")
		return output