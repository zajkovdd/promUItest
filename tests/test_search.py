import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import WebDriverException, TimeoutException

from core.BaseFunctions import browser
from pages.BasePage import BasePageHelper
from pages.SearchPage import SearchPageHelper

BASE_URL = 'https://promminer.ru/'
SEARCH_TEXT = 'S19J'

@allure.suite('Тестирование Поиска')
@allure.title('Позитивный сценарий: Поиск S19J')
def test_search_positive(browser):

    BasePage = BasePageHelper(browser)
    SearchPage = SearchPageHelper(browser)

    # Шаг 1: Открытие страницы
    try:
        with allure.step("Открытие страницы promminer.ru"):
            BasePage.get_url(BASE_URL)
            BasePage.attach_screenshot()
    except WebDriverException as e:
        allure.attach(f"Ошибка при открытии страницы: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось открыть страницу: {str(e)}")

    # Шаг 2: Нажатие на кнопку поиска
    try:
        BasePage.click_search()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку поиска: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось найти или кликнуть на кнопку поиска: {str(e)}")

    # Шаг 3: Ввод текста в поле поиска
    try:
        BasePage.type_search(SEARCH_TEXT)
    except TimeoutException as e:
        allure.attach(f"Ошибка при вводе текста в поле поиска: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось ввести текст в поле поиска: {str(e)}")

    # Шаг 4: Нажатие Enter
    try:
        BasePage.type_enter()
    except TimeoutException as e:
        allure.attach(f"Ошибка при нажатии Enter: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось нажать Enter: {str(e)}")

    # Шаг 5: Проверка страницы результатов поиска
    try:
        SearchPage.check_page()
    except TimeoutException as e:
        allure.attach(f"Ошибка при проверке страницы результатов: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        SearchPage.attach_screenshot()
        pytest.fail(f"Не удалось проверить страницу результатов: {str(e)}")






