from selenium.webdriver.common.by import By
from pages.homepage import HomePage

class MovieDetailPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.species_list = (By.XPATH, "//h1[text()='Species']/following::ul[1]/li")
        self.planets_list = (By.XPATH, "//h1[text()='Planets']/following::ul[1]/li")
        self.back_button = (By.XPATH, "//button[contains(text(),'Back')]")

    def get_species(self):
        self.wait_for_elements(self.species_list)
        return [elem.text.strip() for elem in self.driver.find_elements(*self.species_list)]

    def get_planets(self):
        self.wait_for_elements(self.planets_list)
        return [elem.text.strip() for elem in self.driver.find_elements(*self.planets_list)]

    def click_back(self):
        self.driver.find_element(*self.back_button).click()
        


