import allure

from selenium.webdriver.common.by import By


from pages.BasePage import BasePageHelper


class ComparePageLocators:
    PAGE_LOCATOR = (By.XPATH, '//*[@id="bx_catalog_compare_block"]/div/div[1]/div/div/label')
    FIRST_ASIC_LOCATOR = (By.XPATH, '//*[@id="bx_560410812_5253"]/div/div[2]/div[1]/div/div/div/a')
    SECOND_ASIC_LOCATOR = (By.XPATH, '//*[@id="bx_560410812_5234"]/div/div[2]/div[1]/div/div/div/a')


class ComparePageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(ComparePageLocators.PAGE_LOCATOR)
        self.find_element(ComparePageLocators.FIRST_ASIC_LOCATOR)
        self.find_element(ComparePageLocators.SECOND_ASIC_LOCATOR)






