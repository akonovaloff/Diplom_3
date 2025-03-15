class Locators:

    class Header:
        constructor = "//p[text()='Конструктор']"
        feed = "//p[text()='Лента Заказов']"
        login = "//p[text()='Личный Кабинет']"
        logo = "//*[contains(@class, 'AppHeader_header__logo__')]"

    class Constructor:
        ingredients_box = "//div[contains(@class, 'BurgerIngredients_ingredients')]"
        buns = "//span[text()='Булки']"
        sauces = "//span[text()='Соусы']"
        fillings = "//span[text()='Начинки']"
        upper_bun = "//span[text()='Перетяните булочку сюда (верх)']"
        lower_bun = "//span[text()='Перетяните булочку сюда (низ)']"
        all_ingredients = "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"
        ingredient_popup_window = "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]"
        ingredient_popup_close_button = f"{ingredient_popup_window}/../button"
        ingredient_name = "//p[contains(@class, 'BurgerIngredient_ingredient__text')]"
        basket_price = "//p[contains(@class, 'BurgerConstructor_basket__totalContainer')]//p[contains(@class, 'text')]"
        order_button = "//button[text()='Оформить заказ']"
        ingredient_counter = "//p[contains(@class, 'counter_counter__num')]"
        basket_field = "//ul[contains(@class, 'BurgerConstructor_basket')]"
        order_popup_window = "//div[contains(@class, 'Modal_modal__container__')]"


    class Account:
        login_to_account_button = "//button[text()='Войти в аккаунт']"

    class Feed:
        feed_box = "//div[contains(@class, 'OrderFeed_contentBox')]"

    class Login:
        email_input = "//input[@name='name']"
        password_input = "//input[@name='Пароль']"
        login_button = "//button[text()='Войти']"
        show_password_button = f"{password_input}/..//*[local-name()='svg']"
        registration_link = "//*[@href='/register']"