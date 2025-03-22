import allure
from selenium.webdriver.common.by import By

from src.pages.header_page import HeaderPage
from src.helpers.urls import Urls


class ForgotPasswordPage(HeaderPage):
    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[@href='/forgot-password']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__container']//*[local-name()='svg']")
    PASSWORD_INPUT = (By.XPATH, f"{SHOW_HIDE_PASSWORD_BUTTON[1]}/../..//input")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTRATION_LINK = (By.XPATH, "//*[@href='/register']")
    RESTORE_BUTTON = (By.XPATH, "(//button)[1]")

    @allure.step("Создать страницу «Восстановить пароль»")
    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url not in [Urls.forgot_password_page, Urls.reset_password_page, Urls.login_page]:
            self.click_on_header__account_button()
            self.wait_for_loading_animation()

    @allure.step("Перейти на страницу авторизации")
    def goto_login_page(self):
        self.goto_page(Urls.login_page)

    @allure.step("Перейти на страницу восстановления пароля")
    def goto_forgot_password_page(self):
        self.goto_page(Urls.forgot_password_page)

    @allure.step("Клик по ссылке «Восстановить пароль»")
    def click_on_forgot_password_link(self):
        self.click_on(self.FORGOT_PASSWORD_LINK)

    @allure.step("Ввод email")
    def enter_email(self, email: str):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке «Восстановить»")
    def click_on_restore_button(self):
        self.click_on(self.RESTORE_BUTTON)
        self.wait_for_url_to_be(Urls.reset_password_page)

    @allure.step("Перейти на страницу сброса пароля")
    def get_reset_password_page(self):
        self.goto_page(Urls.forgot_password_page)
        self.click_on_restore_button()
        self.wait_for_url_to_be(Urls.reset_password_page)

    def get_password_field_type(self):
        _password_field = self.find_element(self.PASSWORD_INPUT)
        return _password_field.get_attribute("type")

    @allure.step("Клик «Показать/скрыть пароль»")
    def click_on_show_hide_password_button(self):
        _button = self.click_on(self.SHOW_HIDE_PASSWORD_BUTTON)
