from ..settings import API_NAME, API_VERSION, API_DESCRIPTION
from typing import Dict

HOMEPAGE_RESPONSE: Dict[str, str] = {
    "message": f"Welcome to {API_NAME}! {API_DESCRIPTION} Explore current game giveaways from various sources.",
    "available_routes": {
        "/home": f"The default page of the {API_NAME} {API_VERSION}",
        "/api_info": "Returns details about the API itself.",
        "/docs": "Explore the API documentation for detailed usage instructions.",
        "/redoc": "An alternative API documentation interface.",
        "/giveaways_all": "Retrieves the current game giveaways. ",
        "/giveaway/{store_name}": "Retrieves the filtered giveaways.",
    }
}
