class ExCollection():
	def __init__(self):
		self.datasets = []

	def collect(self, dataset):
		for x in dataset.data:
			x.__dict__.update(dataset._metadata.__dict__)
		self.datasets.extend(dataset.data)
		# for d in dataset.data:
		# 	for attr, value in vars(d).items():
		# 		# print(f"{attr}: {value}")

		# for attr, value in vars(dataset._metadata).items():
		# 	for x in dataset.data:
		# 		setattr(x, attr, value)
		# self.datasets.extend(dataset.data)
				# print(f"{attr}: {value}")


		# to_collect = [setattr(x, attr, value) for x in dataset.data for attr, value in vars(dataset._metadata).items()]


		# dataset.data is a list of objects. i want to mutate each object

		# for x in ex_data:


		# for x in dataset.data:
			# print(x)
		# for i in to_collect:
		# 	print(i)