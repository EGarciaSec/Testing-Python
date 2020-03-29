import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import chromedriver_binary 


def setup_driver():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome("C:\\Users\\Usuario\\Testing-Python\\resources\\chromedriver", chrome_options=chrome_options)
	return driver


def test_simple_load():
	driver = setup_driver()
	driver.get("https://egarciasec.github.io/pdex/")
	assert driver.find_element_by_xpath('//*[@id="root"]/h1')
	driver.quit()

def test_pokemon_search():
	driver = setup_driver()
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
	driver.quit() 
