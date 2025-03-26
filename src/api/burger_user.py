from faker import Faker
from src.api.burger_api import BurgerApi as Api


class BurgerUser:
    fake = Faker("en-US")
    api = Api

    def __init__(self):

        self.email: str = ""
        self.password: str = ""
        self.name = "TestUser"

        self.generate_email()
        self.generate_password()

        self.__server_email: str = self.email
        self.__server_name: str = self.name
        self.__server_password: str = self.password
        self.__is_registered = False
        self.access_token: str = ""
        self.__refresh_token: str = ""

        self._payload = self.Payload(self)  # Инициализируем вложенный класс
        print(self)

    def __del__(self):
        if self.__is_registered:
            response = self.api.delete_user(self.access_token)

    def __repr__(self):
        return f"StellarBurgerUser: {self.payload.full}"

    def generate_email(self):
        self.email = self.fake.ascii_email()

    def generate_password(self):
        self.password = self.fake.password(8)

    def generate_name(self):
        self.name = self.fake.first_name()

    @property
    def payload(self):
        # Возвращаем экземпляр Payload, чтобы можно было обращаться к no_password, no_email и т.д.
        return self._payload

    class Payload:
        def __init__(self, user):
            self.user = user

        @property
        def full(self):
            # Возвращает полный словарь
            return {
                "email": self.user.email,
                "password": self.user.password,
                "name": self.user.name
            }


    def registration(self):
        response = self.api.register_user(self.payload.full)
        if response.success:
            self.__is_registered = True
            self.access_token = response.data['accessToken']
            self.__refresh_token = response.data['refreshToken']
            self.__update_server_info()
        else:
            # Сгенерировать новый email и перезапустить регистрацию
            self.generate_email()
            response = self.registration()
        return response


    def __update_server_info(self):
        is_info_updated = False
        if self.__server_name != self.name:
            is_info_updated = True
            self.__server_name = self.name
        if self.__server_password != self.password:
            is_info_updated = True
            self.__server_password = self.password
        if self.__server_email != self.email:
            is_info_updated = True
            self.__server_email = self.email
        if is_info_updated:
            print(self)
