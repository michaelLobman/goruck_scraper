from scraper.scraper import Scraper
from merger.merger import Merger
from aggregator.aggregator import Aggregator 

class Executor:
	def __init__(self, keyword):
		self._scraper = Scraper()
		self._merger = Merger()
		self._aggregator = Aggregator(keyword)


	def execute_all(self,):
		self._scraper.execute()
		self._merger.execute()
		self._aggregator.execute()

	def execute_archive(self):
		self._scraper.scrape_archive()

	def execute_aggregator(self):
		self._aggregator.execute()