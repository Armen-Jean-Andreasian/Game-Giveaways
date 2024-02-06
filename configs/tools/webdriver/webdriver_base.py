from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from configs.constants import WebDriverConstants


class WebdriverBase:
    __slots__ = ("options", "service", "driver")

    def __init__(self):
        self.options: webdriver.ChromeOptions = None
        self.service: Service = None
        self.driver: webdriver.Chrome = None

    def __initialize_options(self):
        """
        Initializes Chrome-driver's options
            - Works with in-project Google Chrome
        :return:
        """
        self.options = webdriver.ChromeOptions()

        # connecting GoogleChrome.exe
        self.options.binary_location = WebDriverConstants.GOOGLE_CHROME_PATH

        # self.options.add_argument("--headless")

        # setting full-screen
        self.options.add_argument("start-maximized")

        # turns off "is controlled by software"
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        return self

    def __initialize_services(self):
        self.service = Service(executable_path=WebDriverConstants.CHROMEDRIVER_PATH)
        return self

    def initialize_webdriver(self):
        """Initializes the Selenium webdriver using Chrome."""
        self.__initialize_options()
        self.__initialize_services()

        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        return self

    def close_tab(self):
        self.driver.close()
        return self

    def quit_webdriver(self):
        self.driver.quit()
        return self
