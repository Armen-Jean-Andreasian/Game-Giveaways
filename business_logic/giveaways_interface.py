from business_logic.models.steam import Steam
from business_logic.models.epic_games import EpicGames
from configs.constants.api.responses import API_RESPONSE_SAMPLE
from configs.constants import EPIC_GAMES_RESPONSE_KEY, STEAM_RESPONSE_KEY

class Giveaways:
    @staticmethod
    def get_current_giveaways() -> dict:
        steam_store_obj = Steam()
        epic_games_obj = EpicGames()

        steam_giveaways = steam_store_obj.get_giveaways()
        epic_giveaways = epic_games_obj.get_giveaways()

        api_response = API_RESPONSE_SAMPLE.copy()
        response = dict()

        response.update(steam_giveaways)
        response.update(epic_giveaways)
        api_response['response'] = response

        return api_response
