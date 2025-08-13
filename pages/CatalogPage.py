import allure

from selenium.webdriver.common.by import By


from pages.BasePage import BasePageHelper


class CatalogPageLocators:
    PRICE_LOCATOR = (By.XPATH, '//*[@id="main"]/div[5]/div[4]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div[1]/div[1]/text()')
    FIRST_GOOD_COMPARE_BUTTON = (By.XPATH, '//*[@id="bx_3966226736_5253"]/div/div[4]/div/div[2]/div[2]/a')
    SECOND_GOOD_COMPARE_BUTTON = (By.XPATH, '//*[@id="bx_3966226736_5234"]/div/div[4]/div/div[2]/div[2]/a')

class CatalogPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(CatalogPageLocators.PRICE_LOCATOR)

    def click_compare_first_button(self):
        self.find_element(CatalogPageLocators.FIRST_GOOD_COMPARE_BUTTON).click()

    def click_compare_second_button(self):
        self.find_element(CatalogPageLocators.SECOND_GOOD_COMPARE_BUTTON).click()




