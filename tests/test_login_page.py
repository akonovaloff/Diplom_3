import pytest
from conftest import new_user, existing_user, pw
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.urls import Urls


class TestLoginPage:
    @pytest.fixture(params=["existing_user", (pytest.param("new_user", marks=pytest.mark.xfail))])
    def user(self, request, new_user, existing_user):
        user_type = request.param
        if user_type == "new_user":
            pytest.mark.xfail(reason="User is not registered. The test MUST be failed", strict=False)
            return new_user
        else:
            return existing_user

    def test_login_to_account(self, user, pw):
        page = LoginPage(pw)
        page.email_input.type(user.email)
        page.password_input.type(user.password)
        page.login_button.click()
        expect(page.pw).to_have_url(Urls.main_url, timeout=3000)
        page.header.login_button.click()
        expect(page.pw).to_have_url(Urls.profile, timeout=3000)
        expect(page.pw.locator(f"//*[@value='{user.email}']")).to_be_visible()


