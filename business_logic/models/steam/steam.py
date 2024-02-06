import re

from business_logic.interfaces import WebsiteParserInterface
from configs.constants import SteamConstants
from configs.shared_scripts.file_manager import DataSaver


class SteamBase(WebsiteParserInterface):
    URL = SteamConstants.url
    HTML_BLOCK_TAG_NAME = SteamConstants.html_block_tag_name
    HTML_BLOCK_TAG_VALUE = SteamConstants.html_block_tag_value
    HTML_OUTPUT_FOLDER = SteamConstants.html_output_folder

    def extract_image_links(self):
        app_id_pattern = re.compile(r'/app/(\d+)/')
        image_url_template = "https://cdn.akamai.steamstatic.com/steam/apps/{}/header.jpg"
        if self.links:
            for link in self.links:
                app_id_finding = app_id_pattern.search(link)
                app_id = app_id_finding.group(1)
                formatted_image_url = image_url_template.format(app_id)
                self.image_links.append(formatted_image_url)
        return self

    def extract_links(self):
        super().extract_links()
        return self

    def extract_text(self):
        """Extracts text outta BeautifulSoup.Tag """
        try:
            title_elements = self.soup.findAll(name='span', class_="title")
            self.titles = [title.get_text(strip=True) for title in title_elements]
        except Exception:
            raise "Giveaway not found"

    def extract_data(self):
        self.extract_text()
        self.extract_links()
        self.extract_image_links()


class SteamMain(SteamBase):
    def request_data(self):
        # scrapping the giveaway html block
        self.scrap_html(tag_name=self.HTML_BLOCK_TAG_NAME, tag_value=self.HTML_BLOCK_TAG_VALUE)

        # make soup
        self.make_soup()

        # extracting data
        self.extract_data()
        # saving extracted data
        data_saver_object = DataSaver(html_content=self.giveaway_html_block,
                                      text_content=",".join(self.titles),
                                      folder_file_path=SteamBase.HTML_OUTPUT_FOLDER)
        data_saver_object.save_results()
        return self

    def send_data(self) -> dict:
        zipped_games = list(zip(self.titles, self.image_links, self.links))

        api_response = []

        for title, image_url, game_url in zipped_games:
            game_data = {'title': title, 'image_url': image_url, 'game_url': game_url}
            api_response.append(game_data)

        return {"steam_giveaways": api_response}


class Steam:
    __slots__ = ['steam_main',]

    def __init__(self):
        self.steam_main = SteamMain()

    def get_giveaways(self):
        self.steam_main.request_data()
        return self.steam_main.send_data()
