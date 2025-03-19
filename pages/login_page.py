from pages.base_page import BasePage, Page
from utils.urls import Urls
from pages.locators import Locators as Loc
from api.burger_user import BurgerUser

class LoginPage(BasePage):
    url = Urls.login
    locators = Loc.Login

    def __init__(self, pw: Page):
        super().__init__(pw)
        if self.pw.url != self.url:
            self.header.login_button.click()
        self.pw.wait_for_load_state(state="networkidle", timeout=5000)
        assign_element = lambda loc: self.pw.locator(loc)
        self.email_input = assign_element(self.locators.email_input)
        self.password_input = assign_element(self.locators.password_input)
        self.login_button = assign_element(self.locators.login_button)
        self.show_password_button = assign_element(self.locators.show_password_button)
        self.registration_link = assign_element(self.locators.registration_link)
        self.restore_password_link = assign_element(self.locators.restore_password_link)

    def login_user(self):
        user = BurgerUser()
        response = user.registration()
        assert response.success, "The user must be registered before tests"
        page = LoginPage(self.pw)
        page.email_input.type(user.email)
        page.password_input.type(user.password)
        page.login_button.click()
        page.pw.wait_for_selector(Loc.Constructor.order_button, state="visible")