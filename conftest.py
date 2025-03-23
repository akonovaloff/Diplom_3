import pytest
from selenium import webdriver
from src.api.burger_user import BurgerUser
from src.pages.constructor_page import ConstructorPage
from src.pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def registered_user() -> BurgerUser:
    """Generate new user data: email, password, name"""
    user = BurgerUser()
    user.registration()
    return user


@pytest.fixture()
def page_with_order(driver, registered_user):
    PersonalAccountPage(driver).login_user(registered_user)
    ConstructorPage(driver).make_an_order()
