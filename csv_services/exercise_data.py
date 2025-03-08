class ExerciseData():
	def __init__(self, id, dataset, exercise, reps):
		self.id = dataset.id
		self.date = dataset.date
		self.rx = dataset.rx
		self.rounds = dataset.rounds or None
		self.duration = dataset.duration or None
		self.exercise = exercise
		self.reps = reps