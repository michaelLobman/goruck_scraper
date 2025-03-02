from datetime import datetime
import requests
from bs4 import BeautifulSoup

def vested():
	with open("goruck_flattened", "r") as read_file:
		with open("goruck_vest", "w", encoding="utf-8") as write_file:
			for workout in read_file:
				if "vest" in workout.lower():
					split_workout = workout.split("///")
					for line in split_workout:
						if "\"" in line:

						write_file.write(line)
						write_file.write("\n")
					write_file.write("\n")
	print("Vested")



def format():
	with open("goruck_2025-02-28", "r") as file:
		with open("goruck_sanitized", "w", encoding="utf-8") as new_file:
			for line in file:
				if "###" in line:
					stripped = line.replace("###", "").strip()
					stripped = stripped + "\n"
					new_file.write(stripped)
				else:
					new_file.write(line)
	print("done")

def flattened():
	with open("goruck_sanitized", "r") as file:
		with open("goruck_flattened", "w", encoding="utf-8") as new_file:
			clean_text = ""
			for line in file:
				stripped = line.strip()
				if not stripped and clean_text:
					new_file.write(clean_text)
					new_file.write("\n")
					clean_text = ""
				else:
					if clean_text:
						stripped += "///"
					clean_text += stripped
	print("done")

