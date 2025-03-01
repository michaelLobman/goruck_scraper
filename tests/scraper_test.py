import unittest
from scraper import scraper

class TestScraper(unittest.TestCase):
	def test_instatiation():
		test_object = Scraper(False)
		self.assertEqual(test_object.last_workout, '02.28.2025 "VESTED DT"')

if __name__ == "__main__":
	unittest.main()