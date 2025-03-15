from pages.base_page import BasePage
from utils.urls import Urls
from pages.locators import Locators as Loc


class ConstructorPage(BasePage):
    url = Urls.main_url
    locators = Loc.Constructor

    def assign_page_elements_by_locators(self):
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

    @staticmethod
    def get_quantity(ingredient) -> str:
        return ingredient.locator(Loc.Constructor.ingredient_counter).text_content()

    def add_ingredient_to_basket(self, ingredient):
        ingredient.scroll_into_view_if_needed()
        self.pw.locator(Loc.Constructor.ingredient_popup_window).locator("..//button").click()
        print(self.get_quantity(ingredient))
        ingredient.drag_to(self.basket_field)
