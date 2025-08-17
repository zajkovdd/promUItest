

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import WebDriverException, TimeoutException

from conftest import browser
from pages.BasePage import BasePageHelper
from pages.CatalogPage import CatalogPageHelper
from pages.ComparePage import ComparePageHelper

BASE_URL = 'https://promminer.ru/'

@allure.suite('Тестирование Сравнения')
@allure.title('Позитивный сценарий: Добавление двух ASIC для сравнения')
def test_compare_two_asic_positive(browser):

    BasePage = BasePageHelper(browser)
    CatalogPage = CatalogPageHelper(browser)
    ComparePage = ComparePageHelper(browser)

    # Шаг 1: Открытие базовой страницы
    try:
        with allure.step(f"Открытие страницы {BASE_URL}"):
            BasePage.get_url(BASE_URL)
            BasePage.attach_screenshot()
    except WebDriverException as e:
        allure.attach(f"Ошибка при открытии страницы: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось открыть страницу {BASE_URL}: {str(e)}")

    # Шаг 2: Клик по кнопке каталога
    try:
        BasePage.click_catalog()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку каталога: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку каталога: {str(e)}")

    # Шаг 3: Клик по кнопке ASIC
    try:
        BasePage.click_asic_button()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку ASIC: {str(e)}")

    # Шаг 4: Клик по кнопке сравнения для первого элемента
    try:
        CatalogPage.click_compare_first_button()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на первую кнопку сравнения: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на первую кнопку сравнения: {str(e)}")

    # Шаг 5: Клик по кнопке сравнения для второго элемента
    try:
        CatalogPage.click_compare_second_button()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на вторую кнопку сравнения: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на вторую кнопку сравнения: {str(e)}")

    # Шаг 6: Клик по кнопке сравнения
    try:
        CatalogPage.click_compare()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку сравнения: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку сравнения: {str(e)}")

    # Шаг 7: Проверка страницы сравнения
    try:
        ComparePage.check_page()
    except TimeoutException as e:
        allure.attach(f"Ошибка при проверке страницы сравнения: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        ComparePage.attach_screenshot()
        pytest.fail(f"Не удалось проверить страницу сравнения: {str(e)}")








