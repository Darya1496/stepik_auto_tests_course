import pytest
from self import self

from stepik_auto_tests_course.pages.main_page import MainPage
from stepik_auto_tests_course.pages.locators import Magasin
from stepik_auto_tests_course.pages.base_page import BasePage
from stepik_auto_tests_course.pages.product_page import ProductPageLocators


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу

    page.should_be_add_to_basket()

    assert not page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented"


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу

    assert not page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу

    page.should_be_add_to_basket()

    assert not page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented"
