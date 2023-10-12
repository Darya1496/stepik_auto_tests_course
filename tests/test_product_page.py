import pytest
from self import self

from stepik_auto_tests_course.pages.login_page import LoginPage
from stepik_auto_tests_course.pages.main_page import MainPage
from stepik_auto_tests_course.pages.locators import Magasin
from stepik_auto_tests_course.pages.base_page import BasePage
from stepik_auto_tests_course.pages.product_page import ProductPageLocators
from stepik_auto_tests_course.tests.conftest import browser


class TestUserAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_user_cant_see_success_message(self):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(self,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

        assert not page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    @pytest.mark.need_review
    def test_user_can_go_to_login_page(self):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(self, link)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page2 = BasePage

        page.should_be_add_to_basket()

        page.solve_quiz_and_get_code()

    @pytest.fixture(scope="function", autouse=True)  # добавить фикстуру сетап. внутри нее
    def setup(self):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"  # открыть страницу регистрации
        page = LoginPage(browser, link)
        page.register_new_user()  # зарегать нового пользователя
        page.should_be_authorized_user()  # проверить что пользователь залогинен