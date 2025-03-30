from scraper.scraper import Scraper
from merger.merger import Merger
from converter.converter import Converter

class Executor:
	def __init__(self):
		self._scraper = Scraper()
		self._merger = Merger()
		self._converter = Converter()

	def execute_all(self):
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