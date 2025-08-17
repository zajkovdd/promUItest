

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import WebDriverException, TimeoutException

from conftest import browser
from pages.BasePage import BasePageHelper
from pages.CatalogPage import CatalogPageHelper
from pages.FavoritePage import FavoritePageHelper

BASE_URL = 'https://promminer.ru/'

@allure.suite('Тестирование Избранного')
@allure.title('Позитивный сценарий: Добавление двух ASIC в избранное и удаление')
def test_favourite_two_asic_positive(browser):

    BasePage = BasePageHelper(browser)
    CatalogPage = CatalogPageHelper(browser)
    FavoritePage = FavoritePageHelper(browser)

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
        with allure.step("Клик по кнопке каталога"):
            BasePage.click_catalog()
            BasePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку каталога: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку каталога: {str(e)}")

    # Шаг 3: Клик по кнопке ASIC
    try:
        with allure.step("Клик по кнопке ASIC"):
            BasePage.click_asic_button()
            BasePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        BasePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку ASIC: {str(e)}")

    # Шаг 4: Клик по кнопке добавления первого ASIC в избранное
    try:
        with allure.step("Клик по кнопке добавления первого ASIC в избранное"):
            CatalogPage.click_favourite_first_button()
            CatalogPage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на первую кнопку избранного: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на первую кнопку избранного: {str(e)}")

    # Шаг 5: Переход в раздел избранного
    try:
        with allure.step("Переход в раздел избранного"):
            CatalogPage.click_favourite()
            CatalogPage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при переходе в раздел избранного: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось перейти в раздел избранного: {str(e)}")

    # Шаг 6: Проверка наличия первого ASIC в избранном
    try:
        with allure.step("Проверка наличия первого ASIC в избранном"):
            FavoritePage.check_first_asic()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при проверке первого ASIC в избранном: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось проверить первый ASIC в избранном: {str(e)}")

    # Шаг 7: Клик по кнопке каталога для возврата
    try:
        with allure.step("Клик по кнопке каталога для возврата"):
            FavoritePage.click_catalog()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку каталога: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку каталога: {str(e)}")

    # Шаг 8: Клик по кнопке ASIC для возврата в каталог
    try:
        with allure.step("Клик по кнопке ASIC для возврата в каталог"):
            FavoritePage.click_asic_button()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку ASIC: {str(e)}")

    # Шаг 9: Клик по кнопке добавления второго ASIC в избранное
    try:
        with allure.step("Клик по кнопке добавления второго ASIC в избранное"):
            CatalogPage.click_favourite_second_button()
            CatalogPage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на вторую кнопку избранного: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на вторую кнопку избранного: {str(e)}")

    # Шаг 10: Переход в раздел избранного
    try:
        with allure.step("Переход в раздел избранного"):
            CatalogPage.click_favourite()
            CatalogPage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при переходе в раздел избранного: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        CatalogPage.attach_screenshot()
        pytest.fail(f"Не удалось перейти в раздел избранного: {str(e)}")

    # Шаг 11: Проверка наличия первого ASIC в избранном
    try:
        with allure.step("Проверка наличия первого ASIC в избранном"):
            FavoritePage.check_first_asic()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при проверке первого ASIC в избранном: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось проверить первый ASIC в избранном: {str(e)}")

    # Шаг 12: Проверка наличия второго ASIC в избранном
    try:
        with allure.step("Проверка наличия второго ASIC в избранном"):
            FavoritePage.check_second_asic()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при проверке второго ASIC в избранном: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось проверить второй ASIC в избранном: {str(e)}")

    # Шаг 13: Клик по кнопке удаления первого ASIC из избранного
    try:
        with allure.step("Клик по кнопке удаления первого ASIC из избранного"):
            FavoritePage.click_first_asic_unfavorite_button()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку удаления первого ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку удаления первого ASIC: {str(e)}")

    # Шаг 14: Проверка отсутствия первого ASIC в избранном
    try:
        with allure.step("Проверка отсутствия первого ASIC в избранном"):
            assert FavoritePage.check_first_asic_absent(), "Первый ASIC все еще присутствует в избранном"
            FavoritePage.attach_screenshot()
    except AssertionError as e:
        allure.attach(f"Ошибка при проверке отсутствия первого ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось подтвердить отсутствие первого ASIC: {str(e)}")

    # Шаг 15: Клик по кнопке удаления второго ASIC из избранного
    try:
        with allure.step("Клик по кнопке удаления второго ASIC из избранного"):
            FavoritePage.click_second_asic_unfavorite_button()
            FavoritePage.attach_screenshot()
    except TimeoutException as e:
        allure.attach(f"Ошибка при клике на кнопку удаления второго ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось кликнуть на кнопку удаления второго ASIC: {str(e)}")

    # Шаг 16: Проверка отсутствия второго ASIC в избранном
    try:
        with allure.step("Проверка отсутствия второго ASIC в избранном"):
            assert FavoritePage.check_second_asic_absent(), "Второй ASIC все еще присутствует в избранном"
            FavoritePage.attach_screenshot()
    except AssertionError as e:
        allure.attach(f"Ошибка при проверке отсутствия второго ASIC: {str(e)}",
                      name="Error Log",
                      attachment_type=AttachmentType.TEXT)
        FavoritePage.attach_screenshot()
        pytest.fail(f"Не удалось подтвердить отсутствие второго ASIC: {str(e)}")








