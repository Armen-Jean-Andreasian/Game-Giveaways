from .api.settings import API_NAME, API_VERSION, API_DESCRIPTION
from .api.settings import SUPPORTED_STORES
from .api.settings import WHITELISTED_IP_ADDRESSES
from .api.settings import CACHE_FILE_PATH
from .api.settings import ERROR_LOG_FILE_PATH, INFO_LOG_FILE_PATH

from .api.routes import ALL_GIVEAWAYS_ROUTE, QUERIED_GIVEAWAY_ROUTE
from .api.routes import API_INFO_ROUTE, HOMEPAGE_ROUTE_V1, HOMEPAGE_ROUTE_V2

from .api.responses import API_RESPONSE_SAMPLE, HOMEPAGE_RESPONSE
from .api.responses import ALL_GIVEAWAYS_DEFAULT_RESPONSE
from .api.responses import STEAM_RESPONSE_KEY, EPIC_GAMES_RESPONSE_KEY, GOG_RESPONSE_KEY

# store info to scap
from .backend.store_data import SteamConstants
from .backend.store_data import GogConstants
from .backend.store_data import EpicGamesConstants
# scrapper constants
from .backend.selenium import WebDriverConstants
