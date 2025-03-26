import time

from src.pages.feed_page import FeedPage
from src.helpers.urls import Urls

import allure


class TestFeedPage:
    @allure.title("Тест: клик по заказу открывает всплывающее окно с деталями")
    def test_order_info_by_click_on_order_list_item(self, driver):
        page = FeedPage(driver)
        page.click_on_order(49)
        assert page.wait_for_element_to_be_visible(page.ORDER_INFO)
