from scraper.scraper import Scraper
from merger.merger import Merger

class Executor:
	def __init__(self):
		self._scraper = Scraper()
		self._merger = Merger()

	def execute_all(self):
		self._scraper.execute()
		self._merger.execute()