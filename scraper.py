import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

if __name__ == "__main__":
	url = "https://noblemtl.com/childhood-friend-of-the-zenith-chapter-198/"
	
	page_to_scrape = webdriver.Chrome()
	page_to_scrape.get(url)
	time.sleep(20)
	# page = driver.page_source
	# soup = BeautifulSoup(page, "html.parser")

	# all_divs = soup.find('tbody', {'class' : 'rankings-app-body'})
	# game_profiles = all_divs.find_all('div', {'class' : 'regular-info-container'})
	# print(game_profiles)