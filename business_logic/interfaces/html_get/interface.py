from .script import ScraperManager
from ..base import StoreBase

class WebsiteScrapperInterface(StoreBase):
    def scrap_html(self, tag_name, tag_value):
        """
        Initializes the Scraper object via the Manager class.
        Scraps the website, takes and assigns the HTML code to StoreBase.giveaway_html_block
        """

        scrapper = ScraperManager(url=self.URL, root_elem_tag_name=tag_name, root_elem_tag_value=tag_value)

        try:
            self.giveaway_html_block = scrapper.get_website()
        except Exception:
            raise "Giveaway not found"
        return None
