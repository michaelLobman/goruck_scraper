import unittest
from scraper.scraper import Scraper

class TestScraper(unittest.TestCase):
	def test_instatiation(self):
		print("testing test_instatiation")
		test_object = Scraper(False)
		self.assertEqual(test_object.final_workout, '02.28.2025 "VESTED DT"')

if __name__ == "__main__":
	unittest.main()