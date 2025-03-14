# -*- coding: utf-8 -*-
from random import randint

import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure


class TestBurgerConstructor:

    @pytest.fixture(autouse=True)
    def open_burger_constructor_page(self, page):
        with allure.step("Open the BurgerConstructor page"):
            page.goto(Urls.main_url)
            allure.attach(page.screenshot(),
                          name="BurgerConstructor_screenshot",
                          attachment_type=allure.attachment_type.PNG)

    @allure.tag("CONSTRUCTOR", "INGREDIENTS_DETAILS")
    @allure.feature("CONSTRUCTOR")
    def test_popup_window_by_ingredient_click(self, page):
        ingredients = page.locator(Loc.Constructor.all_ingredients)
        with allure.step("Select a random ingredient"):
            rand_index = randint(0, ingredients.count())
            ingredient = ingredients.nth(rand_index)
            ingredient.scroll_into_view_if_needed()
            ingredient.hover()
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
            assert popup_window.is_visible()
