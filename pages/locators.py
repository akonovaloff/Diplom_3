class Locators:

    class Header:
        constructor = "//p[text()='Конструктор']"
        feed = "//p[text()='Лента Заказов']"
        login = "//p[text()='Личный Кабинет']"

    class Constructor:
        ingredients_box = "//div[contains(@class, 'BurgerIngredients_ingredients')]"
        buns = "//span[text()='Булки']/.."
        sauces = "//span[text()='Соусы']/.."
        fillings = "//span[text()='Начинки']/.."
        upper_bun = "//span[text()='Перетяните булочку сюда (верх)']"
        lower_bun = "//span[text()='Перетяните булочку сюда (низ)']"
        all_ingredients = "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"
        ingredient_popup_window = "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]"

    class Feed:
        feed_box = "//div[contains(@class, 'OrderFeed_contentBox')]"

    class Login:
        email_input = "//input[@name='name']"
        password_input = "//input[@name='Пароль']"
        login_button = "//button[text()='Войти']"
