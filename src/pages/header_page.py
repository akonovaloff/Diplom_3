import allure

from src.pages.base_page import BasePage
from src.helpers.urls import Urls

from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    HEADER__CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    HEADER__FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    HEADER__ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    HEADER__LOGO_BUTTON = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo__')]")
    LOADING_ANIMATION = (By.XPATH, "//img[@alt='loading animation']")

    @allure.step("Создать страницу")
    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url not in Urls.base_url:
            self.goto_page(Urls.base_url)
            self.wait_for_loading_animation()

    @allure.step("Клик по кнопке «Конструктор»")
    def click_on_header__constructor(self):
        self.click_on(self.HEADER__CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке «Лента заказов»")
    def click_on_header__feed_button(self):
        self.click_on(self.HEADER__FEED_BUTTON)


    @allure.step("Клик по кнопке «Личный кабинет»")
    def click_on_header__account_button(self):
        self.click_on(self.HEADER__ACCOUNT_BUTTON)

