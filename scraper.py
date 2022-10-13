import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

if __name__ == "__main__":
	url = "https://app.sensortower.com/ios/rankings/top/ipad/us/all-categories?date=2022-10-13"
	driver = webdriver.Chrome(executable_path=r"C:\Users\Jin\Documents\GitHub\IosStoreScraper\chromedriver.exe") 
	driver.get(url)
	
	time.sleep(10)

	page = driver.page_source
	soup = BeautifulSoup(page, "html.parser")

	all_divs = soup.find('tbody', {'class' : 'rankings-app-body'})
	game_profiles = all_divs.find_all('div', {'class' : 'regular-info-container'})
	print(game_profiles)