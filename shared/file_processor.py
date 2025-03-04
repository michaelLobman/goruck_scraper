from shared.file_manager import FileManager

class FileProcessor:
	def __init__(self):
		self._prepend = FileManager("to_prepend")
		self._merged = FileManager("merged")
		self._archive = FileManager("archive")