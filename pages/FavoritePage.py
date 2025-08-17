import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePageHelper


class FavoritePageLocators:
    PAGE_LOCATOR = (By.XPATH, '//*[@id="pagetitle"]')
    FIRST_ASIC_LOCATOR = (By.XPATH, '//*[@id="bx_3966226736_5253"]/div/div[3]/div/div/div[2]/a')
    FIRST_GOOD_FAVORITE_BUTTON = (By.XPATH, '//*[@id="bx_3966226736_5253"]/div/div[4]/div/div[2]/div[1]/a')
    SECOND_ASIC_LOCATOR = (By.XPATH, '//*[@id="bx_3966226736_5234"]/div/div[3]/div/div/div[2]/a')
    SECOND_GOOD_FAVORITE_BUTTON = (By.XPATH, '//*[@id="bx_3966226736_5234"]/div/div[4]/div/div[2]/div[1]/a')



class FavoritePageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(FavoritePageLocators.PAGE_LOCATOR)

    def check_first_asic(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(FavoritePageLocators.FIRST_ASIC_LOCATOR)

    def check_second_asic(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(FavoritePageLocators.SECOND_ASIC_LOCATOR)

    def click_first_asic_unfavorite_button(self):
        self.find_element(FavoritePageLocators.FIRST_GOOD_FAVORITE_BUTTON).click()

    def click_second_asic_unfavorite_button(self):
        self.find_element(FavoritePageLocators.SECOND_GOOD_FAVORITE_BUTTON).click()

    def check_first_asic_absent(self, timeout=10):
        with allure.step('Проверяем отсутствие первого ASIC на странице'):
            self.attach_screenshot()
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located(FavoritePageLocators.FIRST_ASIC_LOCATOR)
                )
                return True
            except:
                return False

    def check_second_asic_absent(self, timeout=10):
        with allure.step('Проверяем отсутствие второго ASIC на странице'):
            self.attach_screenshot()
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located(FavoritePageLocators.SECOND_ASIC_LOCATOR)
                )
                return True
            except:
                return False






