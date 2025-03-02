import re
import requests

from pathlib import Path 
from bs4 import BeautifulSoup

from shared.file_utility import FileUtility

# TODO: the scraper should only scrape. it should not have to concern itself with prev content
class Scraper:
	def __init__(self):
		self.count = 0
		self._url = "https://www.goruck.com/blogs/workouts?page="
		self._rel_path = "./files"
		self._dst_name = "goruck_to_prepend.txt"
		self._merged_name = "goruck_merged.txt"
		self.file_utility = FileUtility(self._rel_path)
		self._final_workout = self.set_final_workout()

	@property
	def base_url(self):
		return self._base_url

	@property
	def final_workout(self):
		return self._final_workout

	def set_final_workout(self):
		path = f"{self._rel_path}/{self._merged_name}"
		return self.file_utility.get_first_line(path)

	def execute(self):
		print("copying existed prepend file")
		backup_path = self.file_utility.create_backup(self._dst_name)
		print(f"backup {backup_path} created")
		self.scrape()
		print("scrape successful")

	def scrape(self):
		max_index = 10 # fail safe
		index = 0
		keep_scraping = True;
		while keep_scraping and index < max_index:
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
		if elements:
			dst_path = f"{self._rel_path}/{self._dst_name}"
			with open(dst_path, "a", encoding="utf-8") as file:
				for element in elements:
					for line in element.find_all("p"):
						text = line.get_text(strip=True)
						if text == self._final_workout:
							print("reached last workout - exiting scrape.")
							return False
						print(text)
						file.write(text + "\n")
					file.write("\n\n")
		return True