from scraper.scraper import Scraper
from merger.merger import Merger
from aggregator.aggregator import Aggregator 
from converter.converter import Converter

class Executor:
	def __init__(self, scrape=False):
		self._scrape = scrape
		if self._scrape:
			self._scraper = Scraper()
			self._merger = Merger()
		self._converter = Converter()

	def execute(self):
		if self._scrape:
			self._scraper.execute()
			self._merger.execute()
		self._converter.execute()

	def execute_archive(self):
		self._scraper.scrape_archive()

	def execute_scraper(self):
		self._scraper.execute()

	def execute_merger(self):
		self._merger.execute()

	def execute_converter(self):
		self._converter.execute()