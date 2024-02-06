from configs.constants.api.routes import (
    API_INFO_ROUTE, HOMEPAGE_ROUTE_V1, HOMEPAGE_ROUTE_V2, REDOC_ROUTE, SWAGGER_UI_ROUTE,
    ALL_GIVEAWAYS_ROUTE, QUERIED_GIVEAWAY_ROUTE,
)

BASE_URL = 'http://127.0.0.1:8000'


class Endpoints:
    redoc = BASE_URL + REDOC_ROUTE
    redoc_response_type = str

    swagger_ui = BASE_URL + SWAGGER_UI_ROUTE
    swagger_ui_response_type = str

    api_info = BASE_URL + API_INFO_ROUTE
    api_info_response_type = dict

    giveaways_all = BASE_URL + ALL_GIVEAWAYS_ROUTE
    giveaways_all_response_type = dict

    giveaway_queried_steam = BASE_URL + QUERIED_GIVEAWAY_ROUTE.format(store_name="steam")
    giveaway_queried_steam_response_type = dict

    giveaways_queried_epic_games = BASE_URL + QUERIED_GIVEAWAY_ROUTE.format(store_name="epic_games")
    giveaways_queried_epic_games_response_type = dict

    home_v1 = BASE_URL + HOMEPAGE_ROUTE_V1
    home_v1_response_type = dict

    home_v2 = BASE_URL + HOMEPAGE_ROUTE_V2
    home_v2_response_type = dict
