from datetime import datetime
from pathlib import Path 
import requests
from bs4 import BeautifulSoup
import re

# TODO: the scraper should only scrape. it should not have to concern itself with prev content
class Scraper:
	def __init__(self):
		self.count = 0
		self._url = "https://www.goruck.com/blogs/workouts?page="
		self._dst_file_path= f"./files/goruck_{datetime.now().strftime("%Y-%m-%d")}"
		# if is_archive:
		# 	self._dst_file_path= f"./files/goruck_archive{datetime.now().strftime("%Y-%m-%d")}"
		# 	self._archive_year = 2023
		# 	# self._archive_months = ["december", "november", "october", "september", "august", "july"]
		# 	self._archive_months = ["december"]
		# else:
		self._final_workout = self.set_final_workout()

	@property
	def base_url(self):
		return self._base_url

	# @property
	# def archive_url(self):
	# 	return self._archive_url

	@property
	def final_workout(self):
		return self._final_workout

	def set_final_workout(self):
		directory = Path("./files")
		files = [f for f in directory.iterdir() if f.is_file()]  
		if not files:
			# handle here for no existing files
			# create anew
			return
		src_file_path = max(files, key=lambda f: f.stat().st_mtime)
		with open(src_file_path, "r") as file:
			first_line = file.readline().strip()
			return first_line
	def scrape(self):
		max_index = 10
		if self.is_archive:
			base_url = self._archive_url
			max_index = len(self._archive_months)
		index = 0
		while index < max_index:
			page_num = index+1
			if self.is_archive:
				scrape_url = f"{base_url}{str(self._archive_months[index])}-{self._archive_year}"
			else:
				scrape_url = base_url + str(page_num)
			self.scrape_page_to_file(scrape_url)
			print(f"scraped page {page_num}")
			index+=1
		print("finished scraping")



	def scrape_page_to_file(self, scrape_url):
		print(scrape_url)
		response = requests.get(scrape_url)
		soup = BeautifulSoup(response.text, "html.parser")	
		elements = soup.find_all("div", class_="bggle_text--container")
		if elements:
			with open(self._dst_file_path, "a", encoding="utf-8") as file:
				for element in elements:
					for line in element.find_all("p"):
						text = line.get_text(strip=True)
						if text == self._final_workout:
							print("reached last workout - exiting scrape.")
							return False
						file.write(text + "\n")
					file.write("\n\n")
	# def scrape(self):
	# 	max_index = 10
	# 	if self.is_archive:
	# 		base_url = self._archive_url
	# 		max_index = len(self._archive_months)
	# 	index = 0
	# 	while index < max_index:
	# 		page_num = index+1
	# 		if self.is_archive:
	# 			scrape_url = f"{base_url}{str(self._archive_months[index])}-{self._archive_year}"
	# 		else:
	# 			scrape_url = base_url + str(page_num)
	# 		self.scrape_page_to_file(scrape_url)
	# 		print(f"scraped page {page_num}")
	# 		index+=1
	# 	print("finished scraping")



	# def scrape_page_to_file(self, scrape_url):
	# 	print(scrape_url)
	# 	response = requests.get(scrape_url)
	# 	soup = BeautifulSoup(response.text, "html.parser")	
	# 	# gross refactor pelase
	# 	if self.is_archive:
	# 		elements = soup.find_all("p")
	# 		if elements:
	# 			with open(self._dst_file_path, "a", encoding="utf-8") as file:
	# 				is_in_workout = False
	# 				print(is_in_workout)
	# 				for element in elements:
	# 					text = element.get_text(strip=True)
	# 					if not is_in_workout:
	# 						print("is not in workout")
	# 						pattern = r"\d+\.\d+\.\d+"
	# 						is_in_workout = text.strip() and re.search(pattern, text)
	# 						if (is_in_workout):

	# 							print("is in workout now true")
	# 							print(text)
	# 					if is_in_workout and text:
	# 						i_am_smart = True
	# 						# print(text)
	# 					else:
	# 						is_in_workout = False
	# 					# while is_workout:

	# 					# for line in element.find_all("div"):
	# 					# 	text = line.get_text(strip=True)
	# 					# 	if text == self._final_workout:
	# 					# 		print("reached last workout - adding previous content.")
	# 					# 		file.write(previous_content)
	# 					# 		return False
	# 					# 	file.write(text + "\n")
	# 					# file.write("\n\n")
	# 		else:
	# 			print("no elements")
	# 	else:
	# 		elements = soup.find_all("div", class_="bggle_text--container")

	# 		if elements:
	# 			with open(self._dst_file_path, "a", encoding="utf-8") as file:
	# 				for element in elements:
	# 					for line in element.find_all("p"):
	# 						text = line.get_text(strip=True)
	# 						if text == self._final_workout:
	# 							print("reached last workout - adding previous content.")
	# 							return False
	# 						file.write(text + "\n")
	# 					file.write("\n\n")
	# def scrape(self):
	# 	base_url = self._archive_url if self.is_archive else self._active_url

	# 	has_new_results = True
	# 	index = 0

	# 	while has_new_results and index < 10:
	# 		page_num = index+1
	# 		scrape_url = base_url + str(page_num)
	# 		has_new_results = self.scrape_page_to_file(scrape_url)
	# 		print(f"scraped page {page_num}")
	# 		index+=1
	# 	print("finished scraping")



	# def scrape_page_to_file(self, scrape_url):
	# 	# TODO: probably refactor storing previous for each page scrape...
	# 	workout_class="bggle_text--container"
	# 	response = requests.get(scrape_url)
	# 	soup = BeautifulSoup(response.text, "html.parser")	
	# 	workouts = soup.find_all("div", class_=workout_class)
	# 	if workouts:
	# 		previous_content = ""
	# 		with open(self._dst_file_path, "r") as file:
	# 			previous_content = file.read()
	# 		with open(self._dst_file_path, "w", encoding="utf-8") as file:
	# 			for workout in workouts:
	# 				for line in workout.find_all("p"):
	# 					text = line.get_text(strip=True)
	# 					if text == self._final_workout:
	# 						print("reached last workout - adding previous content.")
	# 						file.write(previous_content)
	# 						return False
	# 					file.write(text + "\n")
	# 				file.write("\n\n")
	# 	else:
	# 		return False