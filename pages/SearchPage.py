import allure

from selenium.webdriver.common.by import By


from pages.BasePage import BasePageHelper


class SearchPageLocators:
    LOCATOR = (By.XPATH, '//*[@id="bx_3966226736_4405"]/div/div[3]/div/div/div[2]/a/span')

class SearchPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(SearchPageLocators.LOCATOR)
