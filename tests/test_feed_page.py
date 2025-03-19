from random import randint
import pytest
import allure
from pages.locators import Locators as Loc
from conftest import pw, FeedPage, feed_page, page_with_user, page_with_order
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from profile_page import ProfilePage
from playwright.sync_api import expect


class TestFeedPage:
    def test_order_popup_window(self, feed_page: FeedPage):
        order = feed_page.order_list.nth(0)
        feed_page.click(order)
        assert feed_page.order_popup.is_visible()

    def test_total_order_counter(self, feed_page: FeedPage):
        total_order_counter_before_order = feed_page.status_total_order_counter.text_content()
        LoginPage(feed_page.pw).login_user()
        ConstructorPage(feed_page.pw).make_order()
        feed_page.click(feed_page.header.feed_button)
        assert feed_page.status_total_order_counter.text_content() > total_order_counter_before_order

    def test_today_order_counter(self, feed_page: FeedPage):
        today_order_counter_before_order = feed_page.status_today_order_counter.text_content()
        LoginPage(feed_page.pw).login_user()
        ConstructorPage(feed_page.pw).make_order()
        feed_page.click(feed_page.header.feed_button)
        assert feed_page.status_today_order_counter.text_content() > today_order_counter_before_order

    def test_order_is_presented_in_preparing_zone(self, feed_page: FeedPage):
        LoginPage(feed_page.pw).login_user()
        ConstructorPage(feed_page.pw).make_order()
        feed_page.click(feed_page.header.feed_button)
        expect(feed_page.status_preparing_orders_list.first).not_to_contain_text("Все текущие заказы готовы!", timeout=20000)
        preparing_order_id = feed_page.status_preparing_orders_list.first.text_content()
        first_id = feed_page.order_number.nth(0).text_content().replace("#", "")
        second_id = feed_page.order_number.nth(1).text_content().repalce("#", "")
        third_id = feed_page.order_number.nth(2).text_content().replace("#", "")


        assert preparing_order_id in [first_id, second_id, third_id]
        # order_id = ProfilePage(feed_page.pw).get_order_id(0)
        # expect(feed_page.status_preparing_orders_list.get_by_text(order_id)).to_be_visible()
