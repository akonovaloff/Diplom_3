# -*- coding: utf-8 -*-
import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure


class TestHeader:
    @pytest.mark.parametrize("from_url,     element_to_click,       to_url,         necessary_element_locator", [
                            [Urls.feed,     Loc.Header.constructor, Urls.main_url,  Loc.Constructor.ingredients_box],
                            [Urls.feed,     Loc.Header.feed,        Urls.feed,      Loc.Feed.feed_box],
                            [Urls.feed,     Loc.Header.login,       Urls.login,     Loc.Login.email_input],
                            [Urls.login,    Loc.Header.constructor, Urls.main_url,  Loc.Constructor.ingredients_box],
                            [Urls.login,    Loc.Header.feed,        Urls.feed,      Loc.Feed.feed_box],
                            [Urls.login,    Loc.Header.login,       Urls.login,     Loc.Login.email_input],
                            [Urls.main_url, Loc.Header.constructor, Urls.main_url, Loc.Constructor.ingredients_box],
                            [Urls.main_url, Loc.Header.feed, Urls.feed, Loc.Feed.feed_box],
                            [Urls.main_url, Loc.Header.login, Urls.login, Loc.Login.email_input],
    ])
    # <!-- anchor test_transition_by_click_on_element -->
    def test_transition_by_click_on_element(self, page, from_url: str, element_to_click: str, to_url: str,
                                            necessary_element_locator: str):
        """
        The test checks the transition to the destination page after clicking on the element:
        1. Opens the source page (from_url), waits for the element to be visible (element_to_click), hovers the cursor and takes a screenshot.
        2. Performs a click on an element (element_to_click).
        3. Checks redirection to to_url, waits for the required element to be visible (necessary_element_locator), takes a screenshot and checks for the element.
        """
        # Prepare Allure titles and labels
        element_name = element_to_click.split("'")[1]
        site_handle = "site" + from_url.replace(Urls.main_url, "")
        allure.dynamic.title(
            f"Test Transition by click on '{element_name}' from url: '{site_handle}'")
        allure.dynamic.feature("HEADER", element_name)
        allure.dynamic.tag("HEADER", element_name)
        # Starting the test
        with allure.step("Open the from_url page"):
            # Open the from_url page
            page.goto(from_url)
            # Waiting for element_to_click is visible
            element = page.locator(element_to_click)
            element.wait_for(timeout=5000, state="visible")
            # Bring the cursor to the element
            element.hover()
            # Take the from_page screenshot
            allure.attach(page.screenshot(),
                          name="from_page_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Click on the element_to_click"):
            # click
            allure.attach(element.screenshot(),
                          name="element_to_click_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            element.click()

        with allure.step("Checking the destination page"):
            # User must be redirected to the burger constructor page
            page.wait_for_url(to_url)
            # Waiting for necessary_element is visible
            necessary_element = page.locator(necessary_element_locator)
            necessary_element.wait_for(timeout=5000, state="visible")
            # Take the to_page screenshot
            allure.attach(page.screenshot(),
                          name="to_page_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert necessary_element.count() == 1, f"The necessary element is missing on the page"
