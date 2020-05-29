
class MainPage:
    search_input = '//*[@id="PokeINFO"]/input'
    search_button = '//*[@id="PokeINFO"]/button'
    search_name = '//*[@id="root"]/h2'
    search_image = '//*[@id="root"]/img'
    page_title = '//*[@id="root"]/h1'

    def __init__(self, driver):
        self.driver = driver

    def assert_page_title(self):
        assert self.driver.find_element_by_xpath(self.page_title)

    def search(self, name):
        input_element = self.driver.find_element_by_xpath(self.search_input)
        input_element.clear()
        input_element.send_keys(name)
        search = self.driver.find_element_by_xpath(self.search_button)
        search.click()

    def assert_expected_name(self, expected_name):
        pokemon = self.driver.find_element_by_xpath(self.search_name)
        assert pokemon.text == expected_name

    def assert_pokemon_image(self):
        image_element = self.driver.find_element_by_xpath(self.search_image)
        assert image_element.size['height'] > 0
