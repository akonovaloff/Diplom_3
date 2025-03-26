from src.pages.forgot_password_page import ForgotPasswordPage
from src.helpers.urls import Urls

import allure


class TestForgotPassword:

    @allure.title("Клик по ссылке «Восстановить пароль»")
    def test_click_restore_password_button(self, driver):
        page = ForgotPasswordPage(driver)
        page.click_on_forgot_password_link()

        assert page.driver.current_url == Urls.forgot_password_page

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, driver):
        page = ForgotPasswordPage(driver)
        page.goto_forgot_password_page()
        page.enter_email("test_email@provider.com")
        page.click_on_restore_button()
        assert page.get_current_url() == Urls.reset_password_page

    @allure.title("Клик по кнопке «Показать/скрыть пароль» изменяет видимость пароля")
    def test_show_hide_password(self, driver):
        page = ForgotPasswordPage(driver)
        page.goto_forgot_password_page()
        page.click_on_restore_button()
        page.enter_password('test_password')
        assert page.get_password_field_type() == "password"
        page.click_on_show_hide_password_button()
        assert page.get_password_field_type() == "text"