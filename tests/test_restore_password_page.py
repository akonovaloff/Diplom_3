
import allure

from conftest import pw
from pages.login_page import LoginPage
from utils.urls import Urls
import pytest
from pages.locators import Locators as Loc
from pages.base_page import BasePage



class TestRestorePasswordPage:
    @pytest.fixture()
    def transition_to_forgot_password_page(self, pw):
        """
        A Fixture to open the site's restore password page
        """
        page = LoginPage(pw)
        page.click(page.restore_password_link)
        page.expect_to_have_url(Urls.forgot_password)
        return pw

    @pytest.fixture()
    def transition_to_reset_password_page(self, transition_to_forgot_password_page):
        """
        A Fixture to open the site's forgot password page
        """
        pw = transition_to_forgot_password_page
        page = BasePage(pw)
        button = pw.locator("(//button)[1]")
        page.click(button)
        page.expect_to_have_url(Urls.reset_password)
        return pw

    @allure.tag("restore_password", "PASSWORD")
    @allure.title("Test restore password button")
    def test_click_on_restore_password_button(self, pw):
        """
        1. The test starts from the site login page;
        2. clicks on the restore password link;
        3. and then checks the destination url
        """
        page = LoginPage(pw)
        page.click(page.restore_password_link)
        page.expect_to_have_url(Urls.forgot_password)

    @allure.title("Test forgot password page: type email and click the restore button")
    def test_type_email_and_click_restore(self, transition_to_forgot_password_page):
        """
        1. The test starts from the site forgot password page;
        2. types something to the email field;
        3. clicks on the restore button and then checks url of the destination page
        """
        with transition_to_forgot_password_page as pw:
            page = BasePage(pw)
            email_input = pw.locator("(//input)")
            page.type(email_input, "default_email@provider.com")
            button = pw.locator("(//button)[1]")
            page.click(button)
            page.expect_to_have_url(Urls.reset_password)

    @allure.title("Test show/hide password button")
    def test_show_hide_password_button(self, transition_to_reset_password_page):
        """
        1. The test starts from the site's reset password page;
        2. types something to the password field and checks that the password is not visible;
        3. then it clicks on the show password button and checks that the password is visible
        """

        page = BasePage(transition_to_reset_password_page)
        pass_phrase = "tested_password"
        password_field = page.pw.locator(Loc.Login.password_input)
        page.type(password_field, pass_phrase)

        assert password_field.text_content() != pass_phrase, "Password must be hidden"

        show_pass_btn = page.pw.locator(Loc.Login.show_password_button)
        page.click(show_pass_btn)

        with allure.step("Assert password is visible"):
            allure.attach(password_field.screenshot(),
                          name="password-field-with-shown-password",
                          attachment_type=allure.attachment_type.PNG)
            assert password_field.get_attribute("value") == pass_phrase, "Password must be shown"
