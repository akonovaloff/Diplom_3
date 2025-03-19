from conftest import pw, login_user, existing_user, ProfilePage
from utils.urls import Urls
import pytest


class TestProfilePage:
    @pytest.fixture
    def page_with_user(self, pw, login_user, existing_user) -> ProfilePage:
        playwright = login_user(pw, existing_user)
        page = ProfilePage(playwright)
        return page

    def test_transition_to_user_order_history(self, page_with_user: ProfilePage):
        page_with_user.profile__feed_button.click()
        page_with_user.expect_to_have_url(Urls.order_history)

    def test_user_logout(self, page_with_user, existing_user):
        page_with_user.pw.locator(f"//*[@value='{existing_user.email}']").is_visible(timeout=5000)
        page_with_user.click(page_with_user.profile__logout_button)
        page_with_user.expect_to_have_url(Urls.login)
        page_with_user.click(page_with_user.header.login_button)
        page_with_user.expect_to_have_url(Urls.login)

