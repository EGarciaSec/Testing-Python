import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import chromedriver_binary 

class TestLoad:

	def setup(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(chrome_options=chrome_options)

	def teardown(self):
		self.driver.quit()


	def test_simple_load(self):
		driver = self.driver
		driver.get("https://egarciasec.github.io/pdex/")
		assert driver.find_element_by_xpath('//*[@id="root"]/h1')

	def test_pokemon_search(self):
		driver = self.driver
		driver.get("https://egarciasec.github.io/pdex/")
		input_element = driver.find_element_by_xpath('//*[@id="PokeINFO"]/input')
		input_element.clear()
		input_element.send_keys("bulbasaur")
		search = driver.find_element_by_xpath('//*[@id="PokeINFO"]/button')
		search.click()
		for _ in range(0,3):
			try:
				pokemon = driver.find_element_by_xpath('//*[@id="root"]/h2')
				assert pokemon.text == "#1 Bulbasaur"
				break
			except:
				time.sleep(1)

	def test_pokemon_image(self):
		driver = self.driver
		driver.get("https://egarciasec.github.io/pdex/")
		input_element = driver.find_element_by_xpath('//*[@id="PokeINFO"]/input')
		input_element.clear()
		input_element.send_keys("bulbasaur")
		search = driver.find_element_by_xpath('//*[@id="PokeINFO"]/button')
		search.click()
		for _ in range(0,3):
			try:
				image_element = driver.find_element_by_xpath('//*[@id="root"]/img')
				assert image_element.size['height'] > 0
				break
			except:
				time.sleep(1)
