from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.urls import Urls


class BurgerConstructorPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, Urls.main_url)
