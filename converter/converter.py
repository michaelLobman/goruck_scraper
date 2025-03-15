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