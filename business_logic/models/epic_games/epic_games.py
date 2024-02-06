from business_logic.interfaces import WebsiteParserInterface
from configs.constants import EpicGamesConstants
from configs.shared_scripts.file_manager import DataSaver


class EpicGamesBase(WebsiteParserInterface):
    URL = EpicGamesConstants.url
    HTML_BLOCK_TAG_NAME = EpicGamesConstants.html_block_tag_name
    HTML_BLOCK_TAG_VALUE = EpicGamesConstants.html_block_tag_value
    HTML_OUTPUT_FOLDER = EpicGamesConstants.html_output_folder

    def extract_links(self):
        super().extract_links()
        for index, link in enumerate(self.links):
            self.links[index] = 'https://store.epicgames.com' + link
        return self

    def extract_image_links(self):
        image_link_value = 'css-1b2k567'
        image_link_tag = 'img'

        image_links = self.soup.findAll(image_link_tag, class_=image_link_value)
        for image in image_links:
            # Extracting title and src attributes
            title = image.get('alt', '')
            src = image.get('src', '')

            self.titles.append(title)
            self.image_links.append(src)
        return self

    def extract_text(self):
        """The implementation of Epic Games Store doesn't need to do it, as
        the text could be found with image_links, which assigns the title as well"""
        pass

    def extract_data(self):
        print('EpicGamesBase.extract_data')
        self.extract_text()
        self.extract_links()
        self.extract_image_links()


class EpicGames(EpicGamesBase):
    def request_data(self):
        print('EpicGames.request_data')
        # scrapping the giveaway html block
        self.scrap_html(tag_name=self.HTML_BLOCK_TAG_NAME, tag_value=self.HTML_BLOCK_TAG_VALUE)

        # make soup
        self.make_soup()

        # extracting data
        self.extract_data()
        # saving extracted data
        data_saver_object = DataSaver(html_content=self.giveaway_html_block,
                                      text_content=",".join(self.titles),
                                      folder_file_path=self.HTML_OUTPUT_FOLDER)
        data_saver_object.save_results()
        return self

    def send_data(self) -> dict:
        print('EpicGames.send_data')
        print((self.titles, self.image_links, self.links))

        zipped_games = list(zip(self.titles, self.image_links, self.links))

        api_response = []

        for title, image_url, game_url in zipped_games:
            game_data = {'title': title, 'image_url': image_url, 'game_url': game_url}
            api_response.append(game_data)

        return {"epic_games_giveaways": api_response}


    def get_giveaways(self):
        self.request_data()
        return self.send_data()
