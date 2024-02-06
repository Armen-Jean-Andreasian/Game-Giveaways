from .html_get import WebsiteScrapperInterface
from .html_parse import HtmlParserInterface
from abc import ABC


class WebsiteParserInterface(WebsiteScrapperInterface, HtmlParserInterface, ABC):
    pass
