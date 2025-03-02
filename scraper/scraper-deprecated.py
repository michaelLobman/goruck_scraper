from datetime import datetime
from pathlib import Path 
import requests
from bs4 import BeautifulSoup

class Scraper:
	def __init__(self, is_archive):
		self.is_archive = is_archive
		self.count = 0
		self._active_url = "https://www.goruck.com/blogs/workouts?page="
		self._archive_url = "https://www.goruck.com/blogs/news-stories/daily-wod-"
		self._dst_file_path= f"./files/goruck_{datetime.now().strftime("%Y-%m-%d")}"

		if is_archive:
			self._dst_file_path= f"./files/goruck_archive{datetime.now().strftime("%Y-%m-%d")}"
			self._archive_year = 2023
			self._archive_months = ["december", "november", "october", "september", "august", "july"]
		self._final_workout = None
		self._src_file_path = None

		self.initialize_file()

	@property
	def base_url(self):
		return self._base_url

	@property
	def archive_url(self):
		return self._archive_url

	@property
	def final_workout(self):
		return self._final_workout

	def initialize_file(self):
		directory = Path("./files")
		files = [f for f in directory.iterdir() if f.is_file()]  
		if not files:
			# handle here for no existing files
			# create anew
			return
		self._src_file_path = max(files, key=lambda f: f.stat().st_mtime)
		self.set_final_workout()
		self.create_dst_file()

	def set_final_workout(self):
		with open(self._src_file_path, "r") as file:
			first_line = file.readline().strip()
			self._final_workout = first_line

	def create_dst_file(self):
  		src = Path(self._src_file_path)  
  		dst = Path(self._dst_file_path) 
  		dst.write_bytes(src.read_bytes())  

	def scrape(self):
		base_url = self._archive_url if self.is_archive else self._active_url

		has_new_results = True
		index = 0

		while has_new_results and index < 10:
			page_num = index+1
			scrape_url = base_url + str(page_num)
			has_new_results = self.scrape_page_to_file(scrape_url)
			print(f"scraped page {page_num}")
			index+=1
		print("finished scraping")



	def scrape_page_to_file(self, scrape_url):
		# TODO: probably refactor storing previous for each page scrape...
		workout_class="bggle_text--container"
		response = requests.get(scrape_url)
		soup = BeautifulSoup(response.text, "html.parser")	
		workouts = soup.find_all("div", class_=workout_class)
		if workouts:
			previous_content = ""
			with open(self._dst_file_path, "r") as file:
				previous_content = file.read()
			with open(self._dst_file_path, "w", encoding="utf-8") as file:
				for workout in workouts:
					for line in workout.find_all("p"):
						text = line.get_text(strip=True)
						if text == self._final_workout:
							print("reached last workout - adding previous content.")
							file.write(previous_content)
							return False
						file.write(text + "\n")
					file.write("\n\n")
		else:
			return False