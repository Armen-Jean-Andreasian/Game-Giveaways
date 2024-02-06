import json
from configs.constants import CACHE_FILE_PATH
from configs.constants.api.responses import API_RESPONSE_SAMPLE
from .scripts.date_in_usa import date_now, compare_dates


class CacheBase:
    last_request_date_key = 'last_request_date'
    response_key = 'response'

    response_to_send = API_RESPONSE_SAMPLE.copy()
    data_to_save: dict = lambda data, date: {CacheBase.last_request_date_key: date,
                                             CacheBase.response_key: data}

    @classmethod
    def write_data(cls, data: dict) -> None:
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        with open(CACHE_FILE_PATH, "w", encoding="utf-8") as json_file:
            data_to_save = cls.data_to_save(data, date_now())
            json.dump(data_to_save, json_file)

    @classmethod
    def read_data(cls):
        try:
            with open(CACHE_FILE_PATH) as json_file:
                result = json.load(json_file)
        except json.decoder.JSONDecodeError:
            json_file.close()
            cls.write_data(data={})
        return result


class Cache(CacheBase):
    @classmethod
    def get_all_data(cls) -> dict:
        response_to_send = Cache.response_to_send

        try:
            content = cls.read_data()['response']

            response_to_send['response'] = content
            return response_to_send

        except KeyError as error:
            response_to_send['response'] = {"": [error, ]}
            return response_to_send

    @staticmethod
    def get_queried_data(store_key: str) -> dict:
        response_to_send = Cache.response_to_send
        try:
            return Cache.read_data()['response'][store_key]
        except KeyError as error:
            response_to_send['response'] = {"": [error, ]}
            return response_to_send

    @staticmethod
    def is_valid() -> bool:
        """
        Loads store_data from the cache file and return it if the date matches the current date in the USA Eastern Time.
        """
        try:
            cached_date = Cache.read_data().get('last_request_date')
            if compare_dates(cached_date=cached_date):
                return True
        except Exception:
            pass

        return False


if __name__ == '__main__':
    def print_current_cache():
        res = Cache.get_all_data()
        print(res)
        Cache.CACHE_FILE = "cache.json"


    print_current_cache()
