from datetime import datetime

class FileUtility:
	def __init__(self, rel_path):
		self._rel_path = rel_path

	def create_backup(self, src_name):
		now = datetime.now().strftime("%Y-%m-%d")
		src_path = f"{self._rel_path}/{src_name}"
		backup_path = f"{self._rel_path}/backup/{src_name}/{now}"
		src = Path(src_path)  
		backup = Path(backup_path) 
		backup.write_bytes(src.read_bytes()) 
		return backup_path