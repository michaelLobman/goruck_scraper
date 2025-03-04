from shared.file_processor import FileProcessor

class Merger(FileProcessor):
	def __init__(self):
		super().__init__()
		pass

	def merge_files(self):
		with open(self._merged._path, "w") as out, open(self._prepend._path, "r") as f1, open(self._merged._backup_path, "r") as f2:
			for line in f1:
				out.write(line)
			out.write("\n")
			for line in f2:
				out.write(line)	
		print("files merged")

	def execute(self):
		if self._merged.get_first_line() != self._prepend.get_first_line():
			self._merged.create_backup()
			self.merge_files()
		else:
			print("no new data, exiting merge")