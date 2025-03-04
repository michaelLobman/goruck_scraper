from shared.file_processor import FileProcessor
from shared.file_manager import FileManager

class Aggregator(FileProcessor):
	def __init__(self, keyword):
		super().__init__()
		self._keyword = keyword 
		self._file_manager = FileManager(f"by_{keyword}")

	def execute(self):
		print (f"executing aggegator by {self._keyword}")
		self._file_manager.create_backup()
		self.aggregate()
		print("aggregate complete")

	def aggregate(self):
		with open(self._merged._path, "r") as src:
			to_write = []
			workout = []
			is_in_workout = True
			has_keyword = False
			with open(self._file_manager._path, "w", encoding="utf-8") as out:
				for line in src:
					text = line.strip()
					has_keyword = True if self._keyword in text.lower() else has_keyword
					if text and is_in_workout:
						workout.append(text)
					elif text:
						# first line of new workout
						workout = [text]
						is_in_workout = True
					else: # end of workout
						if has_keyword: out.write("\n".join(workout) + "\n\n\n")
						has_keyword = False
						is_in_workout = False
						workout = []
				if has_keyword: out.write("\n".join(workout))
