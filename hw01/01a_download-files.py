# Part 1: Reading some data

# Downloading the data

from requests import get
from bs4 import BeautifulSoup
import wget

url = "https://cslu.ohsu.edu/~bedricks/courses/cs662/hw/HW1/GW-cna_eng/"
response = get(url)

soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all('a'):
	file_name = link.get("href")

	if "cna_eng" in file_name:
		full_url = url + file_name
		file = wget.download(full_url)
	else: 
		continue

