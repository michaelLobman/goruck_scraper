import re
from datetime import datetime
from dateutil import parser

class RegexUtils():

	PATTERNS = {
		"date": r"^\d{1,2}\.\d{1,2}\.\d{1,4}",
		"title": r'(?<=[“""])(.*?)(?=["”"])',
		"rounds": r"(\d+)\s+rounds",
		"ex_reps": r"^\d.*",
		"ex": r"\s.*",
		"reps": r"^\d\S*",
		"rx_plus": r"(?<=rx\+:).*$",
		"rx": r"(?<=rx:).*$",
		"scaled": r"(?<=scaled:).*$",
		"male": r"(?<=male:).*$",
		"female": r"(?<=female:).*$",
		"scoring": r"(?<=scoring=).*",
		"rep_scheme": r"^\d+-\d+-.*",
		"amrap": r"(\d+).*(amrap)",
		"all": r".*"
	}
	GROUP1 = ["rounds", "amrap"]

	@staticmethod
	def try_match(line, key):
		pattern = RegexUtils.PATTERNS[key]
		sanitized_line = line.lower().strip()
		match = re.search(pattern, sanitized_line)
		if not match:
			return None
		output = match.group().strip()
		if key in RegexUtils.GROUP1:
			output = match.group(1)
		elif key == "date":
			output = parser.parse(output)
		return output