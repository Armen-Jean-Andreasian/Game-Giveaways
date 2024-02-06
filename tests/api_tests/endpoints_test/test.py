import requests
from endpoints import Endpoints
import json

class ApiIsOff(Exception):
    def __str__(self):
        return "Turn on API before testing it!"

class Requester:
    @staticmethod
    def get(url, resp_type: type):
        try:
            response = requests.get(url)

            if resp_type is dict:
                try:
                    data = response.json()
                except json.decoder.JSONDecodeError:
                    data = {}  # Пустой словарь, если ответ не содержит JSON
                print(f"Url:{url}, "
                      f"\n\tStatus code:{response.status_code},"
                      f"\n\tResponse:{data}",
                      f"\n")
                return type(data) is resp_type

            elif resp_type is str:
                if response.text:
                    print(f"Url:{url}, "
                          f"\n\tStatus code:{response.status_code},"
                          f"\n\tResponse:Html code"
                          f"\n")
                    return type(response.text) is resp_type
                else:
                    print(f"Url:{url}, "
                          f"\n\tStatus code:{response.status_code},"
                          f"\n\tResponse is empty",
                          f"\n")
                    return False

        except requests.exceptions.ConnectionError:
            raise ApiIsOff




if __name__ == '__main__':
    for attr_name in dir(Endpoints):
        if not attr_name.startswith("__") and not callable(getattr(Endpoints, attr_name)):
            endpoint_url = getattr(Endpoints, attr_name)
            response_type = getattr(Endpoints, f"{attr_name}_response_type")
            try:
                # Assert that the Requester.get() method returns True
                assert Requester.get(endpoint_url, response_type), f"Failed for endpoint: {attr_name}"

            except AssertionError as e:
                print(e)
                exit()
