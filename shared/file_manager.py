class FileManager:
	def __init__(self, name):
		self._timestamp = datetime.now().strftime("%Y-%m-%d")
		self._type = "txt"
		self._name = f"goruck_{self._name}.{self._type}" 
		self._rel_path = "./files"
		self._path = f"{self._rel_path}/{self._name}"
		self._backup_path = f"{self._rel_path}/backups/{self._name}-{self._timestamp}.{self._type}"

	def create_backup(self):
		src = Path(self._path)  
		backup = Path(self._backup_path) 
		backup.write_bytes(src.read_bytes()) 

	def get_first_line(self):
		with open(self._path, "r") as file:
			first_line = file.readline().strip()
			return first_line