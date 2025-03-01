from pathlib import Path 

class Scraper:
	def __init__(self, scrape_archive):
		self.scrape_archive = scrape_archive
		self._base_url = "https://www.goruck.com/blogs/workouts?page="
		self._archive_url = "https://www.goruck.com/blogs/news-stories/daily-wod-"
		self._base_file_name = "goruck"
		self._last_workout = self.set_last_workout()

	def hello_world(self):
		print("Hello world!")
	@property
	def base_url(self):
		return self._base_url

	@property
	def archive_url(self):
		return self._archive_url

	@property
	def last_workout(self):
		return self._last_workout

	def set_last_workout(self):
		directory = Path("./files")
		files = [f for f in directory.iterdir() if f.is_file()]  
		if not files:
			return None  # Return None if no files found
		file_path = max(files, key=lambda f: f.stat().st_mtime)

		with open(file_path, "r") as file:
			first_line = file.readline().strip()
			return first_line

  
 		

	 	# def scrape():
		# 		if is_archive:

		# 		base_url = "https://www.goruck.com/blogs/workouts?page="
		# 		now = datetime.now().strftime("%Y-%m-%d")
		# 		filename = f"goruck_{now}"
		# 		page_num = 1
		# 		workout_count = 0

		# 		open(filename, "w").close()

		# 		while page_num < count:
		# 			url = base_url + str(page_num)
		# 			scrape_page(url, filename)
		# 			print(f"scraped page {page_num}")
		# 			page_num += 1

		# 		print("done scraping")



# def scrape_page(base_url, filename):
# 	workout_class="bggle_text--container"
# 	response = requests.get(base_url)
# 	soup = BeautifulSoup(response.text, "html.parser")	
# 	workouts = soup.find_all("div", class_=workout_class)
# 	with open(filename, "a", encoding="utf-8") as file:
# 		for workout in workouts:
# 			for exercise in workout.find_all("p"):
# 				text = exercise.get_text(strip = True)
# 				is_title = exercise.find("strong")
# 				if is_title:
# 					print(text)
# 				file.write(text + "\n")
			# file.write("\n\n")


		

	# create method for most recent pull

