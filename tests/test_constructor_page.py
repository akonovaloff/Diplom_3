# -*- coding: utf-8 -*-
from random import randint
import pytest
import allure
from pages.locators import Locators as Loc
from conftest import pw, ConstructorPage, constructor_page, Page, ProfilePage, FeedPage
from pages.base_page import expect


class TestConstructorPage:
    number_of_ingredients: int = 3

    @pytest.fixture
    def constructor_page_with_user(self, pw, login_user, existing_user) -> ConstructorPage:
        playwright = login_user(pw, existing_user)
        page = ConstructorPage(playwright)
        page.pw.wait_for_load_state(state="networkidle", timeout=3000)
        return page

    @pytest.fixture()
    def constructor_page_with_order(self, pw: Page, login_user, existing_user, constructor_page_with_user):
        page: ConstructorPage = constructor_page_with_user
        for _ in range(0, 3):
            index = randint(2, 14)
            ingredient = page.all_ingredients.nth(index)
            ingredient.scroll_into_view_if_needed()
            ingredient.drag_to(page.basket_field)
        page.all_ingredients.nth(randint(0, 1)).drag_to(page.basket_field)
        page.pw.wait_for_load_state(state="networkidle", timeout=6000)
        page.click(page.order_button)
        expect(page.order_popup_window).to_be_visible()
        page.order_popup_close_button.click()
        expect(page.order_popup_window).to_be_hidden()
        return page

    @allure.tag("CONSTRUCTOR", "INGREDIENTS_DETAILS")
    @allure.feature("CONSTRUCTOR")
    @pytest.mark.parametrize("ingredient_index", range(0, number_of_ingredients))
    @allure.title("Test Ingredient Pop-up Window")
    def test_ingredients_details_popup_window(self, constructor_page, ingredient_index: int):
        """The test checks the display of a pop-up window with ingredient details in the burger constructor
            for each of the 15 ingredients. The test performs the following steps:
            1. Selects a random ingredient by index (0–14), scrolls it into view, hovers over it,
               saves the ingredient name, and takes a screenshot before clicking.
            2. Performs a click on the selected ingredient.
            3. Verifies the visibility of the pop-up window with ingredient details, takes a screenshot,
               and asserts that the window is displayed.
            4. Verifies that the name of the selected ingredient is visible in the pop-up window."""
        # Select an ingredient
        ingredient = constructor_page.all_ingredients.nth(ingredient_index)
        ingredient_name = ingredient.locator(Loc.Constructor.ingredient_name).text_content()
        allure.dynamic.parameter("ingredient_index", f"{ingredient_index} ({ingredient_name})")
        # Click on the selected ingredient
        constructor_page.click(ingredient)
        # Checking of Pop-up Window
        allure.attach(constructor_page.pw.screenshot(),
                      name="ingredient-popup-screenshot",
                      attachment_type=allure.attachment_type.PNG)
        expect(constructor_page.ingredient_popup_window).to_be_visible()
        # Check the name of selected ingredient in the popup window
        expect(constructor_page.ingredient_popup_window.get_by_text(ingredient_name)).to_be_visible()
        # Close the pop-up
        constructor_page.click(constructor_page.ingredient_popup_close_button)
        expect(constructor_page.ingredient_popup_window).to_be_hidden()

    @pytest.mark.parametrize("ingredient_index", range(0, number_of_ingredients))
    def test_ingredient_counter(self, constructor_page: ConstructorPage, ingredient_index: int):
        ingredient = constructor_page.all_ingredients.nth(ingredient_index)
        ingredient.scroll_into_view_if_needed()
        counter = ingredient.locator(Loc.Constructor.ingredient_counter)
        current_counter_value = int(counter.text_content())
        ingredient.drag_to(constructor_page.basket_field)
        assert int(counter.text_content()) > current_counter_value

    def test_make_order_by_logged_user(self, constructor_page_with_user: ConstructorPage):
        for _ in range(0, 3):
            ingredient_index = randint(0, 14)
            ingredient = constructor_page_with_user.all_ingredients.nth(ingredient_index)
            ingredient.scroll_into_view_if_needed()
            ingredient.drag_to(constructor_page_with_user.basket_field)
        constructor_page_with_user.click(constructor_page_with_user.order_button)
        expect(constructor_page_with_user.order_popup_window).to_be_visible()

    def test_check_order_exists_on_the_feed_page(self, pw: Page, login_user, existing_user, constructor_page_with_user, constructor_page_with_order):
        profile_page = ProfilePage(constructor_page_with_order.pw)
        profile_page.click(profile_page.profile__feed_button)
        order_id = profile_page.feed__order_number.text_content()
        feed_page = FeedPage(profile_page.pw)
        element = feed_page.pw.get_by_text(order_id)
        expect(element).to_be_visible()
