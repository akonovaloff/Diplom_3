class Locators:

    class Header:
        constructor = "//p[text()='Конструктор']"
        feed = "//p[text()='Лента Заказов']"

    class Constructor:
        ingredients_box = "//div[contains(@class, 'BurgerIngredients_ingredients')]"
        buns = "//span[text()='Булки']/.."
        sauces = "//span[text()='Соусы']/.."
        fillings = "//span[text()='Начинки']/.."
        upper_bun = "//span[text()='Перетяните булочку сюда (верх)']"
        lower_bun = "//span[text()='Перетяните булочку сюда (низ)']"

    class Feed:
        feed_box = "//div[contains(@class, 'OrderFeed_contentBox')]"
