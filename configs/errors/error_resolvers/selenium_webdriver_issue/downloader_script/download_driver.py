import os
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.os_manager import OperationSystemManager
from configs.constants import WebDriverConstants

class WebDriverDownloadBase:
    supported_browsers = ("chrome", "opera", "edge")

    def __init__(self):
        self.user_os_name: str
        self.user_browser_name: str
        self.user_browser_version: str
        self.driver_manager = None

    def __detect_user_os(self):
        self.user_os_name = input("OS name? (win, linux, etc): ").lower().strip()
        if self.user_os_name is None:
            pass
        else:
            try:
                OperationSystemManager(os_type=self.user_os_name)
            except Exception:
                exit()
            return self

    def __detect_user_browser_name(self):
        self.user_browser_name = input("Browser name? (chrome, opera, edge): ").lower().strip()

        # browser name check
        if self.user_browser_name not in self.supported_browsers:
            raise Exception(f"Can not get webdriver for {self.user_browser_name}"
                            f"\nSupported browsers: {self.supported_browsers}")
        return self

    def __detect_user_browser_version(self):
        self.user_browser_version = input("Browser version? (117.0.5938.150): ").lower().strip()
        return self

    def initialize_attributes(self):
        self.__detect_user_os()
        self.__detect_user_browser_name()
        self.__detect_user_browser_version()

        if self.user_browser_name == "chrome":
            self.driver_manager = ChromeDriverManager
        elif self.user_browser_name == "opera":
            self.driver_manager = OperaDriverManager
        elif self.user_browser_name == "edge":
            self.driver_manager = EdgeChromiumDriverManager


class WebdriverDownloadHelper(WebDriverDownloadBase):
    def help_me(self):
        """
        Downloads the driver to
        /.wdm/drivers/chromedriver/win64/117.0.5938.150/chromedriver-win32/chromedriver.exe
        """
        self.initialize_attributes()

        os.environ['WDM_LOCAL'] = '1'

        if self.user_os_name is None:
            installment_path = self.driver_manager(driver_version=self.user_browser_version).install()
        else:
            installment_path = self.driver_manager(os_system_manager=OperationSystemManager(os_type=self.user_os_name),
                                                   driver_version=self.user_browser_version).install()

        print("Done!"
              f"\nThe driver is downloaded to {installment_path}"
              f"\nYour next steps are:"
              f"\n1. Move the chromedriver.exe to {WebDriverConstants.webdriver_folder}"
              f"\n2. Delete the folder .wdm\n")

        print("\nATTENTION: If you downloaded not Google Chrome Driver"
              f"\n1. Go to backend/scripts/parser/config/constants.py"
              f"\n2. Find the class WebDriverConstants"
              f"\n3. Change the value of driver_name variable to one you downloaded")


if __name__ == '__main__':
    wbd = WebdriverDownloadHelper()
    wbd.help_me()
