from shared.file_utility import FileUtility
from pathlib import Path 

class Merger:
	def __init__(self):
		self._rel_path = "./files"
		self._prepend_name = "goruck_to_prepend.txt"
		self._merged_name = "goruck_merged.txt"
		self._merged_path = f"{self._rel_path}/{self._merged_name}"
		self._prepend_path = f"{self._rel_path}/{self._prepend_name}"		
		self.file_utility = FileUtility(self._rel_path)
		self._backup_path = None

	def check_new_data(self):
		merged_first_line = self.file_utility.get_first_line(self._merged_path)
		prepend_first_line = self.file_utility.get_first_line(self._prepend_path)

		return merged_first_line != prepend_first_line

	def merge_files(self):
		with open(self._merged_path, "w") as out, open(self._prepend_path, "r") as f1, open(self._backup_path, "r") as f2:
			for line in f1:
				out.write(line)
			out.write("\n")
			for line in f2:
				out.write(line)	
		print("files merged")

	def execute(self):
		has_new_data = self.check_new_data()
		if has_new_data:
			self._backup_path = self.file_utility.create_backup(self._merged_name)
			self.merge_files()
		else:
			print("no new data, exiting merge")