# -*- coding: utf-8 -*-
import pytest

from utils.urls import Urls
from pages.locators import Locators as Loc
import allure


class TestHeaderPage:
    @pytest.fixture(params=[Urls.feed, Urls.login, Urls.main_url], autouse=True)
    def start_page(self, pw, request):
        url: str = request.param
        site_hande = "site" + url.replace(Urls.main_url, "")
        with allure.step(f"Open start pw: {site_hande}"):
            pw.goto(url)

    @pytest.mark.parametrize("element_to_click,         destination_url,        mandatory_element_locator", [
                            [Loc.Header.constructor,    Urls.main_url,          Loc.Constructor.ingredients_box],
                            [Loc.Header.feed,           Urls.feed,              Loc.Feed.Status.status_box],
                            [Loc.Header.login,          Urls.login,             Loc.Login.email_input],
    ])
    def test_header_page(self, pw, element_to_click: str, destination_url,
                         mandatory_element_locator):
        """
        The test checks the transition to the destination pw after clicking on a site header element:
        1. Opens the source pw, waits for the element to be visible (element_to_click), hovers the cursor and takes a screenshot.
        2. Performs a click on an element (element_to_click).
        3. Checks redirection to destination_url, waits for the required element to be visible (mandatory_element_locator), takes a screenshot and checks for the element.
        """
        # Prepare Allure titles and labels
        element_name = element_to_click.split("'")[1]
        destination = "site" + destination_url.replace(Urls.main_url, "")
        allure.dynamic.title(f"Test transitions from header's links")
        allure.dynamic.feature("HEADER", element_name)
        allure.dynamic.tag("HEADER", element_name)
        allure.dynamic.parameter("element_to_click", element_name)
        allure.dynamic.parameter("destination_url", destination)
        allure.dynamic.parameter("mandatory_element_locator", "destination_url:")
        allure.dynamic.parameter("start_page", pw.url.replace(Urls.main_url, ""))

        # Starting the test
        with allure.step("Waiting for element_to_click to be visible"):
            # Waiting for element_to_click is visible
            element = pw.locator(element_to_click)
            element.wait_for(timeout=5000, state="visible")
            # Bring the cursor to the element
            element.hover()
            # Take the from_page screenshot
            allure.attach(pw.screenshot(),
                          name="from_page_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Click on the element_to_click"):
            # click
            allure.attach(element.screenshot(),
                          name="element_to_click_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            element.click()

        with allure.step("Checking the destination pw"):
            # User must be redirected to the burger constructor pw
            pw.wait_for_url(destination_url)
            # Waiting for necessary_element is visible
            necessary_element = pw.locator(mandatory_element_locator)
            necessary_element.wait_for(timeout=5000, state="visible")
            # Take the to_page screenshot
            allure.attach(pw.screenshot(),
                          name="to_page_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert necessary_element.count() == 1, f"The necessary element is missing on the pw"
