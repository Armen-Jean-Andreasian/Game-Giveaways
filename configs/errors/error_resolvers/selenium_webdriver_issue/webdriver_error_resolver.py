from configs.errors.error_resolvers.user_input_reader import UserInputReader
from .downloader_script import WebdriverDownloadHelper
import time


class WebdriverErrorResolver:
    @staticmethod
    def user_option(error):
        """
        Informs the user about the issue with the webdriver and gives 10 seconds to decide
        If the user decides to install the webdriver using WebdriverDownloadHelper - runs the downloader
        If no answer was received or user refused - raises the error
        """

        print(f"{error} occurred, do you want to run the Webdriver Downloader? Y/N")
        waiting_time = 5  # seconds

        start_time = time.time()

        user_input_reader = UserInputReader()
        user_input_reader.start()

        while True:
            if time.time() - start_time > waiting_time:
                raise TimeoutError(f"User did not respond within {waiting_time} seconds.")

            if user_input_reader.is_alive():
                time.sleep(0.1)
            else:
                if user_input_reader.result and user_input_reader.result.strip().lower() == "y":
                    webdriver_download_helper = WebdriverDownloadHelper()
                    webdriver_download_helper.help_me()
                    exit()
                else:
                    raise error
