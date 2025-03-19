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
        order_popup_close_button = f"{order_popup_window}//*[local-name()='svg']"

    class Account:
        login_to_account_button = "//button[text()='Войти в аккаунт']"

    class Feed:
        class Orders:
            order_list = "//li[contains(@class,'OrderHistory_listItem__')]"
            order_number = f"{order_list}//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')]"
            order_price = "//*[@class='OrderHistory_textContainer__3QUXJ']"
            order_popup = "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal__container__Wo2l_']"
            order_popup__order_number = f"{order_popup}//p[@class='text text_type_digits-default mb-10 mt-5']"
            order_popup__close_button = f"{order_popup}//button"

        class Status:
            status_box = "//div[contains(@class, 'OrderFeed_contentBox')]"
            status_total_order_counter = "(//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]"
            status_today_order_counter = "(//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]"
            status_ready_orders_list = "(//ul[contains(@class, 'OrderFeed_orderList__cBvyi')])[1]/li"
            status_preparing_orders_list = "(//ul[contains(@class, 'OrderFeed_orderList__cBvyi')])[2]/li"

    class Login:
        email_input = "//input[@name='name']"
        login_button = "//button[text()='Войти']"
        show_password_button = f"//div[@class='input__container']//*[local-name()='svg']"
        password_input = f"{show_password_button}/../..//input"
        registration_link = "//*[@href='/register']"
        restore_password_link = "//*[@href='/forgot-password']"

    class Profile:
        name_input = "(//input)[1]"
        email_input = "(//input)[2]"
        password_input = "(//input)[3]"
        name_edit_button = f"{name_input}/..//*[local-name()='svg']"
        email_edit_button = f"{email_input}/..//*[local-name()='svg']"
        password_edit_button = f"{password_input}/..//*[local-name()='svg']"
        save_changes_button = "(//button)[3]"
        cancel_changes_button = "(//button)[2]"
        logout_button = "(//button)[1]"
        profile_button = "//*[@href='/account/profile']"
        feed_button = "//*[@href='/account/order-history']"
