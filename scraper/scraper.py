import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from shared.file_utility import FileUtility

class Scraper:
	def __init__(self):
		self.count = 0
		self._url = "https://www.goruck.com/blogs/workouts?page="
		self._rel_path = "./files"
		self._dst_name = "goruck_to_prepend.txt"
		self._merged_name = "goruck_merged.txt"
		self._merged_path = f"{self._rel_path}/{self._merged_name}"
		self.file_utility = FileUtility(self._rel_path)
		self._latest_data = self.set_latest_data()
		self._archive_path = f"{self._rel_path}/goruck_archive.txt"
		self._archive_url = "https://www.goruck.com/blogs/news-stories/daily-wod"
		self._archive_year = 2023
		self._archive_months = ["december", "november", "october", "september", "august", "july"]
		self._archive_pattern = r"^\d{1,2}\.\d{1,2}\.\d{1,2}.*$"

	def set_latest_data(self):
		return self.file_utility.get_first_line(self._merged_path)

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
						if text == self._latest_data:
							print("reached latest_data - exiting scrape.")
							return False
						print(text)
						file.write(text + "\n")
					file.write("\n\n")
		return True

	# Archive methods

	# got the headers

	def scrape_archive(self):
		Path(f"{self._archive_path}").write_text("")
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
		if elements:
			with open(self._archive_path, "a", encoding="utf-8") as file:
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


					# for line in element.find_all("p"):
					# 	text = line.get_text(strip=True)
					# 	if text == self._latest_data:
					# 		print("reached latest_data - exiting scrape.")
					# 		return False
					# 	print(text)
					# 	file.write(text + "\n")
					# file.write("\n\n")
		else:
			print("no elements")


