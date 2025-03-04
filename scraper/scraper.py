import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from shared.file_processor import FileProcessor
class Scraper(FileProcessor):

	def __init__(self):
		super().__init__()
		self._latest_data = self._merged.get_first_line()
		self._url = "https://www.goruck.com/blogs/workouts?page="
		self._archive_url = "https://www.goruck.com/blogs/news-stories/daily-wod"
		self._archive_year = 2023
		self._archive_months = ["december", "november", "october", "september", "august", "july"]
		self._archive_pattern = r"^\d{1,2}\.\d{1,2}\.\d{1,2}.*$"

	def execute(self):
		self._prepend.create_backup()
		self._prepend.clear()
		self.scrape()

	def scrape(self):
		index = 0
		keep_scraping = True;
		while keep_scraping:
			page_num = index+1
			scrape_url = self._url + str(page_num)
			keep_scraping = self.scrape_page_to_file(scrape_url)
			print(f"scraped page {page_num}")
			index+=1
		print("finished scraping")

	def scrape_page_to_file(self, scrape_url):
		print(scrape_url)
		response = requests.get(scrape_url)
		soup = BeautifulSoup(response.text, "html.parser")	
		elements = soup.find_all("div", class_="bggle_text--container")
		with open(self._prepend._path, "a", encoding="utf-8") as file:
			for element in elements:
				for line in element.find_all("p"):
					text = line.get_text(strip=True)
					if text == self._latest_data:
						print("reached latest_data - exiting scrape.")
						return False
					file.write(text + "\n")
				file.write("\n")
		return True

	# Archive methods

	def scrape_archive(self):
		Path(f"{self._archive._path}").write_text("")
		max_index = len(self._archive_months) 
		index = 0
		while index < max_index:
			archive_month = self._archive_months[index]
			append_to_url = f"{archive_month}-{str(self._archive_year)}"
			scrape_url = f"{self._archive_url}-{append_to_url}"
			self.scrape_archive_page_to_file(scrape_url)
			print(f"scraped page {append_to_url}")
			index+=1
		print("finished scraping")

	def scrape_archive_page_to_file(self, scrape_url):
		print(scrape_url)
		response = requests.get(scrape_url)
		soup = BeautifulSoup(response.text, "html.parser")	
		elements = soup.find_all("div", class_="article__body rte")
		with open(self._archive._path, "a", encoding="utf-8") as file:
			is_in_workout = False
			for element in elements:
				counter = 0
				for p in element.find_all("p"):
					text = p.get_text(strip=True)
					# is this the beginning of a workout?
					if text and re.match(self._archive_pattern, text):
						counter = 0
						header = text
						file.write(text + "\n")
						is_in_workout = True
					if is_in_workout and text or counter == 1:
						if p.find("br") and text != header:
							lines = [str(text).strip() for text in p.stripped_strings] 
							for line in lines:
								if line != header: file.write(line + "\n")
							file.write("\n\n")
						elif text and counter == 1:
							file.write(text + "\n\n")
					else:
						is_in_workout = False
					counter += 1