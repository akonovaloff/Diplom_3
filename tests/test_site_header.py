# -*- coding: utf-8 -*-
import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure


class TestSiteHeader:
    @pytest.fixture(params=[Urls.feed, Urls.login, Urls.main_url], autouse=True)
    def from_page(self, page, request):
        url: str = request.param
        site_hande = "site" + url.replace(Urls.main_url, "")
        with allure.step(f"Open start page: {site_hande}"):
            page.goto(url)

    @pytest.mark.parametrize("element_to_click,         to_url,                 necessary_element_locator", [
                            [Loc.Header.constructor,    Urls.main_url,          Loc.Constructor.ingredients_box],
                            [Loc.Header.feed,           Urls.feed,              Loc.Feed.feed_box],
                            [Loc.Header.login,          Urls.login,             Loc.Login.email_input],
    ])
    # <!-- anchor test_transition_by_click_on_element -->
    def test_transition_by_click_on_element(self, page, element_to_click: str, to_url: str,
                                            necessary_element_locator: str):
        """
        The test checks the transition to the destination page after clicking on a site header element:
        1. Opens the source page, waits for the element to be visible (element_to_click), hovers the cursor and takes a screenshot.
        2. Performs a click on an element (element_to_click).
        3. Checks redirection to to_url, waits for the required element to be visible (necessary_element_locator), takes a screenshot and checks for the element.
        """
        # Prepare Allure titles and labels
        element_name = element_to_click.split("'")[1]
        destination = "site" + to_url.replace(Urls.main_url, "")
        allure.dynamic.feature("HEADER", element_name)
        allure.dynamic.tag("HEADER", element_name)
        allure.dynamic.parameter("element_to_click", element_name)
        allure.dynamic.parameter("to_url", destination)
        allure.dynamic.parameter("necessary_element_locator", "page")
        # Starting the test
        with allure.step("Waiting for element_to_click to be visible"):
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
