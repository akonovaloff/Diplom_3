import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from src.api.burger_user import BurgerUser
from src.pages.constructor_page import ConstructorPage
from src.pages.personal_account_page import PersonalAccountPage
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver_path():
    return ChromeDriverManager().install()

@pytest.fixture(params=["chrome"])
def driver(request, driver_path):
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(options=options, service=service)

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
