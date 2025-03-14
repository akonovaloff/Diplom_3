# -*- coding: utf-8 -*-
from random import randint

import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure


class TestBurgerConstructor:

    @pytest.fixture(autouse=True)
    def open_burger_constructor_page(self, page):
        page.goto(Urls.main_url)
        allure.attach(page.screenshot(),
                      name="BurgerConstructor_screenshot",
                      attachment_type=allure.attachment_type.PNG)

    @allure.tag("CONSTRUCTOR", "INGREDIENTS_DETAILS")
    @allure.feature("CONSTRUCTOR")
    @pytest.mark.parametrize("ingredient_index", range(0, 15))
    def test_ingredients_details_popup_window(self, page, ingredient_index: int):
        """The test checks the display of a popup window with ingredient details in the burger constructor
            for each of the 15 ingredients. The test performs the following steps:
            1. Selects a random ingredient by index (0–14), scrolls it into view, hovers over it,
               saves the ingredient name, and takes a screenshot before clicking.
            2. Performs a click on the selected ingredient.
            3. Verifies the visibility of the popup window with ingredient details, takes a screenshot,
               and asserts that the window is displayed.
            4. Verifies that the name of the selected ingredient is visible in the popup window."""

        ingredients = page.locator(Loc.Constructor.all_ingredients)
        with allure.step(f"Select the ingredient with index {ingredient_index}"):
            ingredient = ingredients.nth(ingredient_index)
            ingredient.scroll_into_view_if_needed()
            ingredient.hover()
            ingredient_name = ingredient.locator(Loc.Constructor.ingredient_name).text_content()
            allure.dynamic.parameter("ingredient_index", f"{ingredient_index}. {ingredient_name}")
            allure.attach(ingredient.screenshot(),
                          name="ingredient_before_click_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Click on selected ingredient"):
            ingredient.click()
        with allure.step("Check if popup window is visible"):
            popup_window = page.locator(Loc.Constructor.ingredient_popup_window)
            allure.attach(page.screenshot(),
                          name="page_with_ingredient_details_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert popup_window.is_visible(), "Popup window must be visible"
        with allure.step("Check the ingredient name in the popup window"):
            assert popup_window.get_by_text(
                ingredient_name).is_visible(), "Popup window must contain selected ingredient name"
