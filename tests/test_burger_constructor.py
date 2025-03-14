# -*- coding: utf-8 -*-
from random import randint

import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure


class TestBurgerConstructor:
    number_of_ingredients: int = 15

    @pytest.fixture(autouse=True)
    def open_burger_constructor_page(self, page):
        page.goto(Urls.main_url)
        allure.attach(page.screenshot(),
                      name="BurgerConstructor_screenshot",
                      attachment_type=allure.attachment_type.PNG)

    @allure.tag("CONSTRUCTOR", "INGREDIENTS_DETAILS")
    @allure.feature("CONSTRUCTOR")
    @pytest.mark.parametrize("ingredient_index", range(0, number_of_ingredients))
    @allure.title("Test Ingredient Pop-up Window")
    def test_ingredients_details_popup_window(self, page, ingredient_index: int):
        """The test checks the display of a pop-up window with ingredient details in the burger constructor
            for each of the 15 ingredients. The test performs the following steps:
            1. Selects a random ingredient by index (0–14), scrolls it into view, hovers over it,
               saves the ingredient name, and takes a screenshot before clicking.
            2. Performs a click on the selected ingredient.
            3. Verifies the visibility of the pop-up window with ingredient details, takes a screenshot,
               and asserts that the window is displayed.
            4. Verifies that the name of the selected ingredient is visible in the pop-up window."""
        # Select all ingredients
        ingredients = page.locator(Loc.Constructor.all_ingredients)
        # Select ingredient with index
        with allure.step(f"Select the ingredient with index={ingredient_index}"):
            ingredient = ingredients.nth(ingredient_index)
            ingredient.scroll_into_view_if_needed()
            ingredient.hover()
            ingredient_name = ingredient.locator(Loc.Constructor.ingredient_name).text_content()
            allure.dynamic.parameter("ingredient_index", f"{ingredient_index} ({ingredient_name})")
            allure.attach(ingredient.screenshot(),
                          name="ingredient_before_click_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        # Click on the selected ingredient
        with allure.step("Click on selected ingredient"):
            ingredient.click()
        # Checking of Pop-up Window
        with allure.step("Check if pop-up window is visible"):
            popup_window = page.locator(Loc.Constructor.ingredient_popup_window)
            allure.attach(page.screenshot(),
                          name="page_with_ingredient_details_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert popup_window.is_visible(), "Pop-up window must be visible"
        # Check the name of selected ingredient in the popup window
        with allure.step("Check the ingredient name in the pop-up window"):
            assert popup_window.get_by_text(
                ingredient_name).is_visible(), "Pop-up window must contain selected ingredient name"
        # Close the pop-up
        with allure.step("Close the pop-up window"):
            close_button = popup_window.locator("..//button")
            close_button.hover()
            allure.attach(close_button.screenshot(),
                          name="popup_window_close_button_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            close_button.click()
            page.wait_for_selector(Loc.Constructor.ingredient_popup_window, timeout=3000, state="hidden")
            allure.attach(page.screenshot(),
                          name="closed_popup_window_page_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            # Make sure that the pop-up window can be closed.
            assert popup_window.is_visible() == False, "The pop-up window must be closed"
