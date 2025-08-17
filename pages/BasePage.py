import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePageLocators:
    PROMMINER_LOGO = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[1]/div/div/a/img')
    CATALOG_BUTTON = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[2]/nav/div/div/div/a')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="title-search"]/form/div[1]')
    COMPARE_BUTTON = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[4]/div/div[2]/div/a')
    FAVOURITE_BUTTON = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[4]/div/div[3]/div/a')
    CONTACT_TG_BUTTON = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[4]/div/div[5]/a')
    CONTACT_ME_BUTTON = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[4]/div/div[5]/div[2]')
    TYPE_SEARCH_LOCATOR = (By.XPATH, '//*[@id="title-search-input"]')
    ASICMINERS_BUTTON = (By.XPATH, '//*[@id="main"]/div[5]/div[2]/div[1]/header/div/div[2]/div/div/div[2]/nav/div/div/div/div/div/div/ul/li[1]/div/a/span')

class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.SEARCH_BUTTON)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    def find_element(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f'Не удалось найти элемент {locator}')

    def get_url(self, url):
        return self.driver.get(url)

    def click_search(self):
        self.find_element(BasePageLocators.SEARCH_BUTTON).click()

    def type_search(self, text):
        self.find_element(BasePageLocators.TYPE_SEARCH_LOCATOR).send_keys(text)
        self.attach_screenshot()

    def type_enter(self):
        self.find_element(BasePageLocators.TYPE_SEARCH_LOCATOR).send_keys(Keys.ENTER)
        self.attach_screenshot()

    def click_catalog(self):
        self.find_element(BasePageLocators.CATALOG_BUTTON).click()

    def click_asic_button(self):
        self.find_element(BasePageLocators.ASICMINERS_BUTTON).click()

    def click_compare(self):
        self.find_element(BasePageLocators.COMPARE_BUTTON).click()

    def click_favourite(self):
        self.find_element(BasePageLocators.FAVOURITE_BUTTON).click()




