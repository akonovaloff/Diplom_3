from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.common.by import By


class BasePage:
    driver: WebDriver
    LOADING_ANIMATION = (By.XPATH, "//img[@alt='loading animation']")
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")

    @allure.step("Создать вкладку браузера")
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.driver.maximize_window()

    def set_timeout(self, timeout: int):
        self.wait = WebDriverWait(self.driver, timeout)

    @allure.step("Перейти на страницу")
    def goto_page(self, url: str):
        self.driver.get(url)
        self.wait_for_loading_animation()

    def quit_driver(self):
        self.driver.quit()

    @allure.step("Найти элемент на странице")
    def find_element(self, locator: tuple[str, str], index: int = None) -> WebElement:
        _locator = self.add_index_to_locator(locator, index) if index is not None else locator
        _element = self.wait.until(ec.presence_of_element_located(_locator))
        return _element

    @allure.step("Найти элементы на странице")
    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        _elements = self.wait.until(ec.presence_of_all_elements_located(locator))
        return _elements

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, element) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(ec.visibility_of(element))

    @allure.step("Клик по элементу")
    def click_on(self, locator) -> None:
        _element = self.find_element(locator)
        _element.click()
        self.wait_for_loading_animation()

    @allure.step("Ввод текста")
    def send_keys(self, locator, text: str) -> None:
        _element = self.find_element(locator)
        _element.clear()
        _element.send_keys(text)

    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Ожидание перехода на адрес")
    def wait_for_url_to_be(self, url: str):
        self.wait.until(ec.url_to_be(url), f"\n\tUrl: {self.driver.current_url};\n\texpected: {url}\n")
        self.wait_for_loading_animation()

    @allure.step("Ожидание появления элемента")
    def wait_for_element_to_be_visible(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_to_be_invisible(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator), f"Element {locator[1]} is not clickable")

    @allure.step("Клик по элементу через индекс")
    def click_on_locator_by_index(self, locator: tuple[str, str], index: int) -> WebElement:
        _locator_by_index = self.add_index_to_locator(locator, index)
        _element = self.find_element(_locator_by_index)
        self.scroll_to_element(_element)
        self.click_on(_locator_by_index)
        self.wait_for_loading_animation()
        return _element

    @allure.step("Drag-n-drop")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        self.scroll_to_element(source)
        target = self.find_element(target_locator)
        # копипаста java скрипта
        script = """
                    const ingredient = arguments[0];
                    const orderSection = arguments[1];

                    // Создаем события для перетаскивания
                    const dragStartEvent = new DragEvent('dragstart', { bubbles: true });
                    const dragOverEvent = new DragEvent('dragover', { bubbles: true });
                    const dropEvent = new DragEvent('drop', { bubbles: true });

                    // Инициируем начало перетаскивания
                    ingredient.dispatchEvent(dragStartEvent);

                    // Перетаскиваем в область заказа
                    orderSection.dispatchEvent(dragOverEvent);
                    orderSection.dispatchEvent(dropEvent);
                """
        self.driver.execute_script(script, source, target)
        self.wait_for_loading_animation()
        return source

    @staticmethod
    def add_index_to_locator(locator, index):
        index += 1
        _locator = (locator[0], f"({locator[1]})[{index}]")
        return _locator

    @allure.step("Ожидание анимации загрузки")
    def wait_for_loading_animation(self):
        self.wait_for_element_to_be_invisible(self.LOADING_ANIMATION)

    def find_by_text(self, text: str):
        _locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        return self.find_elements(_locator)

    @allure.step("Ожидание текста в элементе")
    def wait_element_to_have_text(self, locator, text: str):
        self.wait.until(ec.text_to_be_present_in_element(locator, text))
