import allure

from src.api.burger_user import BurgerUser
from src.helpers.urls import Urls
from src.pages.header_page import HeaderPage
from selenium.webdriver.common.by import By
from src.pages.feed_page import FeedPage

class PersonalAccountPage(HeaderPage):
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__container']//*[local-name()='svg']")
    PASSWORD_INPUT = (By.XPATH, f"{SHOW_HIDE_PASSWORD_BUTTON[1]}/../..//input")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//*[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "(//button)[1]")
    ORDER_LOADING_ANIMATION = (By.XPATH, "//*[text()='Загрузка...']")

    ORDER_LIST__ITEMS = FeedPage.ORDER_LIST__ITEMS
    ORDER_LIST__NUMBERS = FeedPage.ORDER_LIST__NUMBERS
    ORDER_INFO = FeedPage.ORDER_INFO
    ORDER_INFO__ORDER_NUMBER = FeedPage.ORDER_INFO__ORDER_NUMBER
    ORDER_INFO__CLOSE_BUTTON = FeedPage.ORDER_INFO__CLOSE_BUTTON

    @allure.step("Создать страницу «Личный кабинет»")
    def __init__(self, driver):
        super().__init__(driver)
        if self.get_current_url() not in [Urls.login_page, Urls.profile_page]:
            self.wait_for_loading_animation()
            self.click_on_header__account_button()


    @allure.step("Ввод email")
    def enter_email(self, email: str):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке «Войти»")
    def click_on_login_button(self):
        self.click_on(self.LOGIN_BUTTON)

    @allure.step("Вход в аккаунт")
    def login_user(self, user: BurgerUser):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_on_login_button()
        self.wait_for_url_to_be(Urls.base_url)

    @allure.step("Клик по кнопке «История заказов»")
    def click_on_order_history_button(self):
        self.wait_for_loading_animation()
        self.click_on(self.ORDER_HISTORY_BUTTON)

    @allure.step("Выход из аккаунта")
    def click_on_logout_button(self):
        self.click_on(self.LOGOUT_BUTTON)

    @allure.step("Получить id заказа")
    def get_order_id(self, index: int) -> str:
        _page_url = self.get_current_url()
        if _page_url not in [Urls.order_history_page, Urls.profile_page]:
            self.click_on_header__account_button()
        if _page_url not in [Urls.order_history_page]:
            self.click_on_order_history_button()
        return self.find_element(self.ORDER_LIST__NUMBERS, index).text.replace("#", "")

    @allure.step("Ожидание статуса заказа")
    def wait_for_order_to_have_status(self, order_index: int, status: str):
        _page_url = self.get_current_url()
        if _page_url not in [Urls.order_history_page, Urls.profile_page]:
            self.click_on_header__account_button()
        if _page_url not in [Urls.order_history_page]:
            self.click_on_order_history_button()
        _order_locator = self.add_index_to_locator(self.ORDER_LIST__ITEMS, order_index)
        self.wait_element_to_have_text(_order_locator, status)