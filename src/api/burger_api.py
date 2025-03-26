import requests
from src.api.burger_api_endpoints import BurgerApiEndpoints as ApiEndpoints
import inspect
import allure


class BurgerApi:
    class HandledResponse:
        def __init__(self, response: requests.Response, success_code: int, show_response: bool = True):
            self.response = response
            self.success = response.status_code == success_code
            self.status_code = response.status_code
            self.text = response.text
            self.__caller = inspect.currentframe().f_back.f_back.f_code.co_name
            try:
                self.data = response.json()
            except requests.exceptions.JSONDecodeError:
                self.data = {}
                print(f"The server returned the data in an unexpected format ({self.__caller}):")
                print(response.text)

            if show_response:
                print(self)

        def __repr__(self):
            return f"{self.__caller}:(success={self.success}, status_code={self.status_code}, data={self.data})"

    @classmethod
    @allure.step("Регистрация нового пользователя")
    def register_user(cls, payload: dict) -> HandledResponse:
        """Отправляет POST-запрос на регистрацию пользователя"""

        response = requests.post(ApiEndpoints.register, json=payload)

        return cls.HandledResponse(response, 200)

    @classmethod
    @allure.step("Удаление пользователя")
    def delete_user(cls, access_token: str) -> HandledResponse:
        """Отправляет DELETE-запрос на удаление пользователя по его accessToken"""

        headers = {"Authorization": access_token}
        response = requests.delete(ApiEndpoints.user, headers=headers)

        return cls.HandledResponse(response, 202)
