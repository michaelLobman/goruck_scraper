import pandas as pd 
import csv
import re
from datetime import datetime
from csv_services.exercise_dataset import ExerciseDataset


class Converter():
	def __init__(self):
		self.all_ex = []

	def execute(self):
		with open("./test_files/convert_test.txt", "r") as txt:
			ex = ExerciseDataset()
			for line in txt:
				if not ex.parse_line(line) and len(ex.data) > 0:
					self.all_ex.extend(ex.data)
					ex = ExerciseDataset()

		df = pd.DataFrame([vars(ex_data) for ex_data in self.all_ex])
		print(df)
			# write to file

	
			# 		# two ways to do this
			# 		# get workout in array, then find all data
			# 		# other is to do it line by line, cleaning the data
			# 		# finding some of it...
			# 		if ""



		# # data = pd.read_csv("./files/goruck_by_vest.txt", sep="\n\n")
		# # print(data)
		# with open ("./files/goruck_by_vest.csv", "w", newline="") as csvfile:
		# 	writer = csv.writer(csvfile)
		# 	writer.writerow(headers)
		# 	with open("./files/goruck_by_vest.txt", "r") as txt:
		# 		is_in_workout = True
		# 		id = 0
		# 		row = []
		# 		date = None
		# 		rounds = None
		# 		# maybe go through entire workout first
		# 		workout = []
		# 		for line in txt:
		# 			stripped = line.strip()
		# 			if not stripped:
		# 				print(workout)
		# 				# writer.writerow(row)
		# 				row = []
		# 				date = None
		# 				rounds = None
		# 				id+=1
		# 				continue
		# 			match = re.search(line, self._date_pattern)
		# 			if match:
		# 				date = datetime.strptime(match.group(), "%Y-%m-%d")
		# 			if "rounds" in line:
		# 				# parse number of roudns


		# # 		print(csvfile)
		# 	# 	is_in_workout = True
		# 	# has_keyword = False
		# 	# with open(self._file_manager._path, "w", encoding="utf-8") as out:
		# 	# 	for line in src:
		# 	# 		text = line.strip()
		# 	# 		text_lower = text.lower()
		# 	# 		has_keyword = True if self._keyword in text_lower else has_keyword
		# 	# 		self._threshold_count += 1 if self._optional and any(optional in text_lower for optional in self._optional) else 0
		# 	# 		if text and is_in_workout:
		# 	# 			workout.append(text)
		# 	# 		elif text:
		# 	# 			# first line of new workout
		# 	# 			workout = [text]
		# 	# 			is_in_workout = True
		# 	# 		else: # end of workout
		# 	# 			if has_keyword or self.meets_threshold: out.write("\n".join(workout) + "\n\n\n")
		# 	# 			has_keyword = False
		# 	# 			is_in_workout = False
		# 	# 			self._threshold_count = 0
		# 	# 			workout = []
		# 	# 	if has_keyword or self._meets_threshold : out.write("\n".join(workout))
