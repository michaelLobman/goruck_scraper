from shared.file_utility import FileUtility
from pathlib import Path 

class Merger:
	def __init__(self):

		self._rel_path = "./files"
		self._prepend_name = "goruck_to_prepend.txt"
		self._merged_name = "goruck_merged.txt"
		self.file_utility = FileUtility(self._rel_path)
		self._backup_path = None

	def execute(self):
		self._backup_path = self.file_utility.create_backup(self._merged_name)
		self.merge_files()

	def merge_files(self):
		merged_path = f"{self._rel_path}/{self._merged_name}"
		prepend_path = f"{self._rel_path}/{self._prepend_name}"

		# need to clean up the open 
		with open(merged_path, "w") as out, open(self.prepend_path, "r") as f1, open(self._backup_path, "r") as f2:
			for line in f1:
				out.write(line)
			out.write("\n")
			for line in f2:
				out.write(line)	
		print("files merged")