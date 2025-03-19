from pages.base_page import BasePage, Page
from utils.urls import Urls
from pages.locators import Locators as Loc
from random import randint
from playwright.sync_api import expect

class ConstructorPage(BasePage):
    url = Urls.main_url
    locators = Loc.Constructor

    def __init__(self, pw: Page):
        super().__init__(pw)
        if self.pw.url != self.url:
            self.header.constructor_button.click()
        self.pw.wait_for_load_state(state="networkidle", timeout=5000)
        assign_element = lambda loc: self.pw.locator(loc)

        self.all_ingredients = assign_element(self.locators.all_ingredients)
        self.basket_field = assign_element(self.locators.basket_field)
        self.basket_price = assign_element(self.locators.basket_price)
        self.buns = assign_element(self.locators.buns)
        self.fillings = assign_element(self.locators.fillings)
        self.ingredient_counter = assign_element(self.locators.ingredient_counter)
        self.ingredient_name = assign_element(self.locators.ingredient_name)
        self.ingredient_popup_close_button = assign_element(self.locators.ingredient_popup_close_button)
        self.ingredient_popup_window = assign_element(self.locators.ingredient_popup_window)
        self.ingredients_box = assign_element(self.locators.ingredients_box)
        self.lower_bun = assign_element(self.locators.lower_bun)
        self.order_button = assign_element(self.locators.order_button)
        self.order_popup_window = assign_element(self.locators.order_popup_window)
        self.sauces = assign_element(self.locators.sauces)
        self.upper_bun = assign_element(self.locators.upper_bun)
        self.order_popup_close_button = assign_element(self.locators.order_popup_close_button)

    @staticmethod
    def get_quantity(ingredient) -> str:
        return ingredient.locator(Loc.Constructor.ingredient_counter).text_content()

    def add_ingredient_to_basket(self, ingredient):
        ingredient.scroll_into_view_if_needed()
        self.pw.locator(Loc.Constructor.ingredient_popup_window).locator("..//button").click()
        print(self.get_quantity(ingredient))
        ingredient.drag_to(self.basket_field)

    def make_order(self):
        page = ConstructorPage(self.pw)
        bun = page.all_ingredients.nth(randint(0, 1))

        sauce = page.all_ingredients.nth(randint(2, 5))

        filling = page.all_ingredients.nth(randint(6, 14))
        for ingredient in [bun, sauce, filling]:
            ingredient.scroll_into_view_if_needed()
            ingredient.drag_to(page.basket_field)

        page.pw.wait_for_load_state(state="networkidle", timeout=6000)
        page.click(page.order_button)
        page.pw.wait_for_timeout(500)
        expect(page.order_popup_window).to_be_visible()
        page.pw.wait_for_load_state(state="networkidle", timeout=3000)
        page.click(page.order_popup_close_button)
        expect(page.order_popup_window).to_be_hidden()



