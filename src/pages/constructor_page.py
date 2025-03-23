from time import sleep
from random import randint

from selenium.webdriver.remote.webelement import WebElement
from src.helpers.urls import Urls
from src.pages.header_page import HeaderPage
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as ec


class ConstructorPage(HeaderPage):
    INGREDIENTS = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']")
    INGREDIENTS_NAMES = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    INGREDIENT_INFO = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]")
    INGREDIENT_INFO__CLOSE_BUTTON = (By.XPATH, f"{INGREDIENT_INFO[1]}/../button")
    INGREDIENT_INFO__INGREDIENT_NAME = (By.XPATH, f"{INGREDIENT_INFO[1]}//p[@class='text text_type_main-medium mb-8']")
    BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__')]")
    ORDER_POPUP_CLOSE_BUTTON = (By.XPATH, f"{ORDER_POPUP[1]}//button")

    @allure.step("Создать страницу «Конструктор»")
    def __init__(self, driver):
        super().__init__(driver)
        if self.get_current_url() not in Urls.base_url:
            self.click_on_header__constructor()
            self.wait_for_loading_animation()

    @allure.step("Клик ингредиента по индексу")
    def click_on_ingredient_by_index(self, index: int) -> WebElement:
        return self.click_on_locator_by_index(self.INGREDIENTS_NAMES, index)

    @allure.step("Закрыть информацию об ингредиенте")
    def close_ingredient_info(self):
        self.click_on(self.INGREDIENT_INFO__CLOSE_BUTTON)

    @allure.step("Добавить булочку")
    def add_bun(self):
        return self.add_ingredient(randint(0, 1))

    @allure.step("Добавить соус")
    def add_sauce(self):
        return self.add_ingredient(randint(2, 4))

    @allure.step("Добавить начинку")
    def add_filling(self):
        return self.add_ingredient(randint(5, 14))

    @allure.step("Добавить ингредиент")
    def add_ingredient(self, index: int):
        _ingredient = self.add_index_to_locator(self.INGREDIENTS, index)
        return self.drag_and_drop(_ingredient, self.BASKET)

    @allure.step("Клик по кнопке «Создать заказ»")
    def click_on_create_order_button(self):
        self.click_on(self.CREATE_ORDER_BUTTON)

    @allure.step("Создать новый заказ")
    def make_an_order(self):
        self.add_bun()
        self.add_sauce()
        self.add_filling()
        self.click_on_create_order_button()
        self.wait_for_element_to_be_visible(self.ORDER_POPUP)
        self.wait_for_loading_animation()
        self.close_order_popup_window()

    @allure.step("Закрыть окно создания заказа")
    def close_order_popup_window(self):
        self.click_on(self.ORDER_POPUP_CLOSE_BUTTON)
