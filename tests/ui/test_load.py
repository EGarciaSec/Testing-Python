import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import chromedriver_binary 
from core.MainPage.page import MainPage

class TestLoad:

	name="Bulbasaur"

	def setup(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get("https://egarciasec.github.io/pdex/")

	def teardown(self):
		self.driver.quit()


	def test_simple_load(self):
		driver = self.driver
		MainPage(driver).assert_page_title()

	def test_pokemon_search(self):
		driver = self.driver
		MainPage(driver).search(self.name)
		for _ in range(0,3):
			try:
				MainPage(driver).assert_expected_name("#1 Bulbasaur")
				break
			except:
				time.sleep(1)

	def test_pokemon_image(self):
		driver = self.driver
		MainPage(driver).search(self.name)
		for _ in range(0,3):
			try:
				MainPage(driver).assert_pokemon_image()
				break
			except:
				time.sleep(1)
