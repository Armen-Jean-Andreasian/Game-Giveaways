from bs4 import BeautifulSoup
from abc import abstractmethod
from business_logic.interfaces.base import StoreBase


class StoreDataExtractor(StoreBase):
    def make_soup(self):
        self.soup = BeautifulSoup(self.giveaway_html_block, 'html.parser')
        return self

    @abstractmethod
    def extract_links(self):
        """Extracts giveaway game links from the BeautifulSoup object"""
        link_tags = self.soup.find_all('a', href=True)
        for tag in link_tags:
            link = tag['href']
            self.links.append(link)
        return self

    @abstractmethod
    def extract_data(self):
        """Abstract method that should run all the extract methods of GiveawayContainerExtractor classes"""
        pass

    @abstractmethod
    def extract_image_links(self):
        """Abstract method that should extract the url-s of game images out of BeautifulSoup.Tag"""
        pass

    @abstractmethod
    def extract_text(self):
        """Abstract method that should extract the text out of BeautifulSoup.Tag (game titles, description, etc) """
        pass
