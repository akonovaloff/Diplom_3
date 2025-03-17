from random import randint
import pytest
import allure
from pages.locators import Locators as Loc
from conftest import pw, FeedPage, feed_page
from pages.base_page import expect

class TestFeedPage:
    def test_order_popup_window(self, feed_page: FeedPage):
        order = feed_page.order_list.nth(0)
        feed_page.click(order)
        assert feed_page.order_popup.is_visible()
