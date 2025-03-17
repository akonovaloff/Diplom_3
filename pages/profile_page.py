from pages.base_page import BasePage, Page
from utils.urls import Urls
from pages.locators import Locators as Loc


class ProfilePage(BasePage):
    url = Urls.profile
    @property
    def locators(self):
        class Locators:
            profile = Loc.Profile
            feed = Loc.Feed.Orders

        return Locators

    def __init__(self, pw: Page):
        super().__init__(pw)
        self.pw.goto(Urls.main_url)
        self.header.login_button.click()
        self.pw.wait_for_load_state(state="networkidle", timeout=5000)
        assign_element = lambda loc: self.pw.locator(loc)
        self.profile__name_input = assign_element(self.locators.profile.name_input)
        self.profile__email_input = assign_element(self.locators.profile.email_input)
        self.profile__password_input = assign_element(self.locators.profile.password_input)
        self.profile__name_edit_button = assign_element(self.locators.profile.name_edit_button)
        self.profile__email_edit_button = assign_element(self.locators.profile.email_edit_button)
        self.profile__password_edit_button = assign_element(self.locators.profile.password_edit_button)
        self.profile__save_changes_button = assign_element(self.locators.profile.save_changes_button)
        self.profile__cancel_changes_button = assign_element(self.locators.profile.cancel_changes_button)
        self.profile__logout_button = assign_element(self.locators.profile.logout_button)
        self.profile__profile_button = assign_element(self.locators.profile.profile_button)
        self.profile__feed_button = assign_element(self.locators.profile.feed_button)

        self.feed__order_list = assign_element(self.locators.feed.order_list)
        self.feed__order_number = assign_element(self.locators.feed.order_number)
        self.feed__order_price = assign_element(self.locators.feed.order_price)
        self.feed__order_popup = assign_element(self.locators.feed.order_popup)
        self.feed__order_popup__order_number = assign_element(self.locators.feed.order_popup__order_number)
        self.feed__order_popup__close_button = assign_element(self.locators.feed.order_popup__close_button)