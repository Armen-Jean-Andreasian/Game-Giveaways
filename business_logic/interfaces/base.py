class StoreBase:
    """Base class of game store_models that keeps all the necessary information for website scrapping"""
    URL: str
    HTML_BLOCK_TAG_NAME: str
    HTML_BLOCK_TAG_VALUE: str
    HTML_OUTPUT_FOLDER: str

    def __init__(self):
        self.giveaway_html_block = None
        self.soup = None
        self.titles = []
        self.links: list = []
        self.image_links: list = []
