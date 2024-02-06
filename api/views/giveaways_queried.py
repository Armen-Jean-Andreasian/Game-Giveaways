from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from configs.constants import QUERIED_GIVEAWAY_ROUTE, API_RESPONSE_SAMPLE, SUPPORTED_STORES
from api.models.documentation_models import GiveawaysQueried

from database.cache import Cache

router = APIRouter()


@router.get(path=QUERIED_GIVEAWAY_ROUTE, response_model=GiveawaysQueried, response_class=JSONResponse,
            tags=["giveaway"], summary="Get giveaways of one store",
            response_description="Retrieve giveaways for the specified store.")
async def get_queried_giveaways(store_name: str) -> dict:
    """
    Get giveaways of one store.

    Retrieve information about giveaways for a specific store.

    :param store_name: The name of the store (e.g., 'steam', 'epic_games').
    :type store_name: str
    :return: Giveaways information for the specified store.
    :rtype: dict
    """
    store_name = store_name.lower().strip()
    print(store_name)

    if store_name not in SUPPORTED_STORES:
        raise HTTPException(status_code=400, detail="Invalid store specified")

    else:
        # accessing out Specific store giveaways data by key
        queried_store_key = store_name + "_giveaways"
        queried_giveaways_data = Cache.get_queried_data(store_key=queried_store_key)

        endpoint_response: dict[str, None] = API_RESPONSE_SAMPLE.copy()

        # Modifying API_RESPONSE_SAMPLE, which is {'response': None},
        endpoint_response['response'] = queried_giveaways_data
        # Making it {'response':{'queried_store_giveaways': []}} then and returning it
        return endpoint_response
