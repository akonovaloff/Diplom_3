from src.pages.header_page import HeaderPage
from src.helpers.urls import Urls

import allure
from selenium.webdriver.common.by import By

class FeedPage(HeaderPage):
    ORDER_LIST__ITEMS = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__')]")
    ORDER_LIST__NUMBERS = (By.XPATH, f"{ORDER_LIST__ITEMS[1]}//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')]")
    ORDER_INFO = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal__container__Wo2l_']")
    ORDER_INFO__ORDER_NUMBER = (By.XPATH, f"{ORDER_INFO[1]}//p[@class='text text_type_digits-default mb-10 mt-5']")
    ORDER_INFO__CLOSE_BUTTON = (By.XPATH, f"{ORDER_INFO[1]}//button")

    ORDERS_IN_PROGRESS = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderList__cBvyi')])[2]/li")
    ORDERS_IS_DONE = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderList__cBvyi')])[1]/li")

    TOTAL_COUNTER = (By.XPATH, "(//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    TODAY_COUNTER = (By.XPATH, "(//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")

    FEED_LOADING_ANIMATION = (By.XPATH, "//*[text()='Загрузка...']")

    @allure.step("Создать страницу «Лента заказов»")
    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url != Urls.feed_page:
            self.click_on_header__feed_button()
            self.wait_for_loading_animation()
            self.wait_for_element_to_be_invisible(self.FEED_LOADING_ANIMATION)

    @allure.step("Клик по заказу")
    def click_on_order(self, index: int):
        return self.click_on_locator_by_index(self.ORDER_LIST__ITEMS, index)

    @allure.step("Получить id заказа")
    def get_order_id(self, index: int):
        return self.find_element(self.ORDER_LIST__NUMBERS, index).text

    @allure.step("Получить текущее значения счетчика «Выполнено за все время»")
    def get_total_counter(self):
        return self.find_element(self.TOTAL_COUNTER).text

    @allure.step("Получить текущее значения счетчика «Выполнено за сегодня»")
    def get_today_counter(self):
        return self.find_element(self.TODAY_COUNTER).text

    @allure.step("Получение списка заказов со статусом «В работе»")
    def get_in_progress_id(self):
        _orders = self.find_elements(self.ORDERS_IN_PROGRESS)
        _id_list = []
        for _order in _orders:
            _id_list.append(_order.text)
        return _id_list

    @allure.step("Ожидание пока заказ получит статус «В работе»")
    def wait_for_order_to_be_in_progress(self, order_id: str):
        _def_timeout = self.timeout
        self.set_timeout(20)
        self.wait_element_to_have_text(self.ORDERS_IN_PROGRESS, order_id)
        self.set_timeout(_def_timeout)

    def wait_for_order_to_be_done(self, order_id: str):
        _def_timeout = self.timeout
        self.set_timeout(20)
        self.wait_element_to_have_text(self.ORDERS_IS_DONE, order_id)
        self.set_timeout(_def_timeout)