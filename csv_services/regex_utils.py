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
		"rx": r"^(rx|male).*$"
	}
	GROUP1 = ["rounds"]

	@staticmethod
	def try_match(line, key):
		pattern = RegexUtils.PATTERNS[key]
		sanitized_line = line.lower().strip()
		match = re.search(pattern, sanitized_line)
		if not match:
			return None
		output = match.group()
		if key in RegexUtils.GROUP1:
			output = match.group(1)
		elif key == "date":
			output = datetime.strptime(output, "%m.%d.%y")
		if key == "rx":
			print(f"rx key matched output: {output}")
		return output