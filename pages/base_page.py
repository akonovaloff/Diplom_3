from playwright.sync_api import Page

class BasePage:
    """
    Базовый класс для всех страниц.
    Инкапсулирует общие методы и функциональность.
    """

    def __init__(self, page: Page, url: str):
        """
        Конструктор базового класса.
        :param page: Экземпляр страницы Playwright.
        """
        self.page = page
        self.page.goto(url)