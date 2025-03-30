import pandas as pd 
import csv
import re
from datetime import datetime
from ex_services.ex_dataset import ExDataset

class Converter():
	def __init__(self):
		self.ex_list = []
		self._df = None
		self._check_cols = ['ex', 'reps']
		self._check_titles = ['suit up']

	def execute(self):
		self.initialize_df()
		self.check_df()
		
	def initialize_df(self):
		with open("./test_files/convert_test.txt", "r") as txt:
			ex = ExDataset()
			for line in txt:
				if not ex.parse_line(line) and len(ex.data) > 0:
					ex.compile_data()
					self.ex_list.extend(ex.data)
					ex = ExDataset()
			if not any(ex._metadata.title == x.title for x in self.ex_list):
				ex.compile_data()
				self.ex_list.extend(ex.data)
		self._df = pd.DataFrame([vars(ex_data) for ex_data in self.ex_list])

	def check_df(self):
		title_filter = self._check_titles or self._df['title'].unique()
		for title in title_filter:
			print(f"___{title}___")
			filtered_by_title = self._df.loc[self._df['title'] == title, self._check_cols]
			print(filtered_by_title)