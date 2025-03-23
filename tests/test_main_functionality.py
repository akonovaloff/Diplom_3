from random import randint

import allure
import pytest

from conftest import registered_user
from src.helpers.urls import Urls
from src.pages.feed_page import FeedPage
from src.pages.personal_account_page import PersonalAccountPage
from src.pages.constructor_page import ConstructorPage


class TestMainFunctionality:
    @pytest.mark.parametrize("start_page", [Urls.base_url,
                                            Urls.feed_page,
                                            Urls.forgot_password_page,
                                            Urls.register_page])
    @allure.title("Переход в раздел «Конструктор» с разных страниц сайта")
    def test_transition_to_constructor_from_header(self, driver, registered_user, start_page: str):
        page = PersonalAccountPage(driver)
        page.login_user(registered_user)
        page.goto_page(start_page)
        page.click_on_header__constructor()
        page.wait_for_url_to_be(Urls.base_url)
        assert page.get_current_url() == Urls.base_url

    @pytest.mark.parametrize("start_page", [Urls.base_url,
                                            Urls.feed_page,
                                            Urls.forgot_password_page,
                                            Urls.register_page])
    @allure.title("Переход в раздел «Лента заказов» с разных страниц сайта")
    def test_transition_to_feed_page_from_header(self, driver, registered_user, start_page: str):
        page = PersonalAccountPage(driver)
        page.login_user(registered_user)
        page.goto_page(start_page)
        page.click_on_header__feed_button()
        page.wait_for_url_to_be(Urls.feed_page)
        assert page.get_current_url() == Urls.feed_page

    @pytest.mark.parametrize("ingredient_index", range(0, 15))
    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_open_ingredient_info(self, driver, ingredient_index: int):
        page = ConstructorPage(driver)
        ingredient_name = page.click_on_ingredient_by_index(ingredient_index).text
        allure.dynamic.parameter("ingredient_index", f"{ingredient_index} - {ingredient_name}")
        ingredient_info = page.wait_for_ingredient_info_popup_window_to_be_visible()
        assert ingredient_name in ingredient_info

    @allure.title("Клик по крестику закрывает всплывающее окно с деталями")
    def test_close_ingredient_info(self, driver):
        page = ConstructorPage(driver)
        page.goto_page(Urls.base_url)
        page.click_on_ingredient_by_index(randint(0, 14))
        page.close_ingredient_info()
        assert page.is_ingredient_info_visible() is False

    @allure.title("Добавление ингредиента увеличивает счетчик")
    def test_adding_an_ingredient_increase_counter(self, driver):
        page = ConstructorPage(driver)
        ingredient_index = randint(2, 14)
        i = 0
        for i in range(1, randint(2, 5)):
            page.add_ingredient(ingredient_index)
        counter = page.get_ingredient_counter(ingredient_index)
        assert counter == i

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, driver, registered_user):
        PersonalAccountPage(driver).login_user(registered_user)
        page = ConstructorPage(driver)
        ConstructorPage(driver).make_an_order()
        assert page.is_order_info_visible()

    @allure.title("Заказы раздела «История заказов» отображаются в «Лента заказов»")
    def test_user_order_history_is_displayed_on_the_feed_page(self, driver, page_with_order):
        page = PersonalAccountPage(driver)
        page.click_on_order_history_button()
        order_number = page.get_order_id(0)
        order = FeedPage(driver).find_by_text(order_number)[0].text
        assert order_number in order

    @allure.title("Новый заказ увеличивает счетчик «Выполнено за все время»")
    def test_total_count(self, driver, registered_user):
        total_counter = FeedPage(driver).get_total_counter()
        PersonalAccountPage(driver).login_user(registered_user)
        ConstructorPage(driver).make_an_order()
        order_id = PersonalAccountPage(driver).get_order_id(0)
        feed_page = FeedPage(driver)
        feed_page.wait_for_order_to_be_done(order_id)
        assert int(FeedPage(driver).get_total_counter()) > int(total_counter)

    @allure.title("Новый заказ увеличивает счетчик «Выполнено за сегодня»")
    def test_today_count(self, driver, registered_user):
        today_counter = FeedPage(driver).get_today_counter()
        PersonalAccountPage(driver).login_user(registered_user)
        ConstructorPage(driver).make_an_order()
        order_id = PersonalAccountPage(driver).get_order_id(0)
        feed_page = FeedPage(driver)
        feed_page.wait_for_order_to_be_done(order_id)
        assert int(FeedPage(driver).get_today_counter()) > int(today_counter)

    @allure.title("Новый заказ появляется в графе «В работе»")
    def test_created_order_displayed_at_in_progress(self, driver, registered_user):
        PersonalAccountPage(driver).login_user(registered_user)
        ConstructorPage(driver).make_an_order()
        order_id = PersonalAccountPage(driver).get_order_id(0)
        feed_page = FeedPage(driver)
        feed_page.set_timeout(20)
        orders_id_list = feed_page.wait_for_order_to_be_in_progress(order_id)
        assert order_id in orders_id_list


