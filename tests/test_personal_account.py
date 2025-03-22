import allure

from src.pages.personal_account_page import PersonalAccountPage
from src.helpers.urls import Urls

class TestPersonalAccount:

    @allure.title("Переход на страницу входа по кнопке «Личный кабинет» из шапки")
    def test_transition_to_login_page_by_click_on_header_link(self, driver):
        page = PersonalAccountPage(driver)
        page.goto_page(Urls.base_url)
        page.click_on_header__account_button()
        page.wait_for_url_to_be(Urls.login_page)


    @allure.title("Вход в аккаунт")
    def test_login_user(self, driver, registered_user):
        page = PersonalAccountPage(driver)
        page.goto_page(Urls.login_page)
        page.login_user(registered_user)
        page.wait_for_url_to_be(Urls.base_url)

    @allure.title("Переход в раздел «История заказов»")
    def test_transition_to_order_history(self, driver, registered_user):
        page = PersonalAccountPage(driver)
        page.goto_page(Urls.login_page)
        page.login_user(registered_user)
        page.click_on_header__account_button()
        page.click_on_order_history_button()
        page.wait_for_url_to_be(Urls.order_history_page)

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, registered_user):
        page = PersonalAccountPage(driver)
        page.goto_page(Urls.login_page)
        page.login_user(registered_user)
        page.click_on_header__account_button()
        page.wait_for_url_to_be(Urls.profile_page)
        page.click_on_logout_button()
        page.wait_for_url_to_be(Urls.login_page)

    @allure.title("Переход в «Личный кабинет» из шапки")
    def test_transition_to_profile_page_by_click_on_header_link(self, driver, registered_user):
        page = PersonalAccountPage(driver)
        page.goto_page(Urls.base_url)
        page.click_on_header__account_button()
        page.login_user(registered_user)
        page.click_on_header__account_button()
        page.wait_for_url_to_be(Urls.profile_page)