from pages.base_page import BasePage, Page
from utils.urls import Urls
from pages.locators import Locators as Loc


class LoginPage(BasePage):
    url = Urls.login
    locators = Loc.Login

    def __init__(self, pw: Page):
        super().__init__(pw, self.url)
        assign_element = lambda loc: self.pw.locator(loc)
        self.email_input = assign_element(self.locators.email_input)
        self.password_input = assign_element(self.locators.password_input)
        self.login_button = assign_element(self.locators.login_button)
        self.show_password_button = assign_element(self.locators.show_password_button)
        self.registration_link = assign_element(self.locators.registration_link)
        self.restore_password_link = assign_element(self.locators.restore_password_link)

