import pandas as pd 
import csv
import re
from datetime import datetime
from csv_services.ex_dataset import ExDataset

class Converter():
	def __init__(self):
		self.ex_list = []
		
	def execute(self):
		last_id = -1
		with open("./test_files/convert_test.txt", "r") as txt:
			ex = ExDataset(last_id)
			for line in txt:
				if not ex.parse_line(line) and len(ex.data) > 0:
					last_id =ex.compile_data()
					self.ex_list.extend(ex.data)
					ex = ExDataset(last_id)
		df = pd.DataFrame([vars(ex_data) for ex_data in self.ex_list])
		print(df)
			# write to file