# -*- coding: utf-8 -*-

import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure
from conftest import constructor_page as page
from pages.base_page import expect


class TestBurgerConstructor:
    number_of_ingredients: int = 15


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
        # Select an ingredient
        ingredient = page.all_ingredients.nth(ingredient_index)
        ingredient_name = ingredient.locator(Loc.Constructor.ingredient_name).text_content()
        allure.dynamic.parameter("ingredient_index", f"{ingredient_index} ({ingredient_name})")
        # Click on the selected ingredient
        page.click(ingredient)
        # Checking of Pop-up Window
        allure.attach(page.pw.screenshot(),
                          name="ingredient-popup-screenshot",
                          attachment_type=allure.attachment_type.PNG)
        expect(page.ingredient_popup_window).to_be_visible()
        # Check the name of selected ingredient in the popup window
        expect(page.ingredient_popup_window.get_by_text(ingredient_name)).to_be_visible()
        # Close the pop-up
        page.click(page.ingredient_popup_close_button)
        expect(page.ingredient_popup_window).to_be_hidden()

