from pages.base_page import BasePage, Page
from utils.urls import Urls
from pages.locators import Locators as Loc


class FeedPage(BasePage):
    url = Urls.feed
    locators = Loc.Feed

    def __init__(self, pw: Page):
        super().__init__(pw)
        if self.pw.url != self.url:
            self.header.feed_button.click()
        self.pw.wait_for_load_state(state="networkidle", timeout=5000)
        assign_element = lambda loc: self.pw.locator(loc)
        # Orders
        self.order_list = assign_element(self.locators.Orders.order_list)
        self.order_number = assign_element(self.locators.Orders.order_number)
        self.order_popup = assign_element(self.locators.Orders.order_popup)
        self.order_popup__order_number = assign_element(self.locators.Orders.order_popup__order_number)
        self.order_popup__close_button = assign_element(self.locators.Orders.order_popup__close_button)
        #Status
        self.status_box = assign_element(self.locators.Status.status_box)
        self.status_total_order_counter = assign_element(self.locators.Status.status_total_order_counter)
        self.status_today_order_counter = assign_element(self.locators.Status.status_today_order_counter)
        self.status_ready_orders_list = assign_element(self.locators.Status.status_ready_orders_list)
        self.status_preparing_orders_list = assign_element(self.locators.Status.status_preparing_orders_list)

