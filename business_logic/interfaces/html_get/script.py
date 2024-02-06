import time
from selenium.webdriver.common.by import By

from configs.constants import WebDriverConstants
from configs.tools.webdriver import WebdriverBase

class WebScrapperCore:
    __slots__ = ['url', 'driver']

    def __init__(self, url: str):
        """Initializes the driver upon URL and provides a scraper interface """
        self.driver = WebdriverBase().initialize_webdriver().driver
        self.url = url

    def get_url(self):
        """Opens the website in Chrome and waits for full page load"""
        self.driver.get(self.url)

    def retrieve_page_html(self) -> str:
        """Retrieves and returns the page source"""
        entire_html = self.driver.page_source
        return entire_html

    def extract_target_block(self, **search_criteria) -> str | None:
        """
        Queries Selenium to detect the needed HTML block.

        Args:
            **search_criteria: The query for Selenium.
                Example: By.CLASS_NAME, "css-2u323"
        """
        giveaway_block_element = self.driver.find_element(**search_criteria)
        giveaway_html_block = giveaway_block_element.get_attribute('outerHTML')
        return giveaway_html_block



class ScraperManager:
    __slots__ = ('web_scrapper', 'root_elem_tag_name', 'root_elem_tag_value', 'html_block')

    def __init__(self, url: str, root_elem_tag_name: str, root_elem_tag_value: str):
        """
        Makes WebScrapperCore work and keeps the results in its state

        Args:
            root_elem_tag_name (str): The HTML tag of the needed HTML block.
            root_elem_tag_value (str): The value of the tag.

        :params:
            element_tag_name : the html tag of the needed html block
            element_value : the value of the tag

        Example:
            <section class="css-2u323">
            Here:
                element_tag_name = "class"
                element_value = "css-2u323"

        """
        self.web_scrapper = WebScrapperCore(url=url)

        self.root_elem_tag_name = root_elem_tag_name
        self.root_elem_tag_value = root_elem_tag_value

        self.html_block = None

    def get_website(self) -> str:
        """
        1. Initializes the webdriver, opens the specified URL.
        2. Retrieves the entire HTML
        3. Tries to retrieve the needed HTML block out of the entire html and reassign to self.html_block.
            3.1 if fails and the block ain't found - passes and leaves to self.html_block with source HTML
            3.2 if succeeds  - self.html_block keeps the HTML code of the needed HTML block

        returns HTML block | source HTML
        """

        self.web_scrapper.get_url()
        time.sleep(WebDriverConstants.TIME_TO_WAIT)

        html_page_source = self.web_scrapper.retrieve_page_html()

        try:
            if self.root_elem_tag_name == "class":
                self.html_block = self.web_scrapper.extract_target_block(by=By.CLASS_NAME, value=self.root_elem_tag_value)
            elif self.root_elem_tag_name == 'id':
                self.html_block = self.web_scrapper.extract_target_block(by=By.ID, value=self.root_elem_tag_value)
            elif self.root_elem_tag_name == 'tag':
                self.html_block = self.web_scrapper.extract_target_block(by=By.TAG_NAME, value=self.root_elem_tag_value)
        except Exception:  # if the needed block ain't found just taking entire HTML code
            self.html_block = html_page_source

        self.web_scrapper.driver.quit()
        return self.html_block
