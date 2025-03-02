from datetime import datetime
from pathlib import Path 


class FileUtility:
	def __init__(self, rel_path):
		self._rel_path = rel_path
		self._file_ext = ".txt"

	def create_backup(self, src_name):
		now = datetime.now().strftime("%Y-%m-%d")
		append = ""
		if self._file_ext in src_name:
			src_name = src_name.replace(self._file_ext, "")
			append = self._file_ext

		src_path = f"{self._rel_path}/{src_name}{append}"
		backup_path = f"{self._rel_path}/backups/{src_name}-{now}{append}"
		src = Path(src_path)  
		backup = Path(backup_path) 
		backup.write_bytes(src.read_bytes()) 
		return backup_path

	def get_first_line(self, path):
		with open(path, "r") as file:
			first_line = file.readline().strip()
			return first_line
