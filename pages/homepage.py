from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.title_header = (By.TAG_NAME, "h1")
        self.table_rows = (By.CSS_SELECTOR, "table tbody tr")
        self.title_header_column = (By.XPATH, "//th[contains(text(), 'Title')]")
        self.empire_strikes_back = (By.XPATH, "//a[text()='The Empire Strikes Back']")
        self.phantom_manace = (By.XPATH, "//a[text()='The Phantom Menace']")

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_all_movie_titles(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))
        return [row.text for row in rows]

    def click_sort_by_title(self):
        self.wait_for_element_visible(self.title_header_column).click()

    def click_empire_strikes_back(self):
        self.wait_for_element_visible(self.empire_strikes_back).click()

    def click_phantom_menace(self):
        self.wait.until(EC.element_to_be_clickable(self.phantom_manace)).click()

    def click_movie_by_title(self, movie_title):
        movie_link = (By.XPATH, f"//a[text()='{movie_title}']")
        try:
            self.wait.until(EC.element_to_be_clickable(movie_link)).click()
        except TimeoutException:
            raise Exception(f"Movie with titel '{movie_title}' not found or not clickable.")










