from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from configs.constants import QUERIED_GIVEAWAY_ROUTE, API_RESPONSE_SAMPLE, SUPPORTED_STORES
from api.models.documentation_models import GiveawaysQueried
from database.cache import Cache
import input_armor


router = APIRouter()


@router.get(path=QUERIED_GIVEAWAY_ROUTE, response_model=GiveawaysQueried, response_class=JSONResponse,
            tags=["giveaway"], summary="Get giveaways of one store",
            response_description="Retrieve giveaways for the specified store.")
async def get_queried_giveaways(store_name: str, request: Request) -> dict:
    """
    Get giveaways of one store.

    Retrieve information about giveaways for a specific store.

    :param store_name: The name of the store (e.g., 'steam', 'epic_games').
    :param request: FastAPI.Request
    :type store_name: str
    :return: Giveaways information for the specified store.
    :rtype: dict
    """
    # security
    check = input_armor.check(rabbit=store_name)
    from api.middleware.request_limiter.requests_archive import RequestsArchive
    client_ip = request.client.host

    # check for malicious input - penalty = permanent ban
    try:
        assert check[True]
    except AssertionError:
        RequestsArchive().block_it(ip=client_ip)
        raise HTTPException(status_code=400, detail="Goodbye. Bye bye")

    # check for correct store name. penalty = waiting time
    store_name = store_name.lower().strip()
    try:
        assert check[True] in SUPPORTED_STORES
    except Exception:
        RequestsArchive().extend_time(ip=client_ip, seconds=5)
        raise HTTPException(status_code=400, detail=f"Invalid store specified. Supported stores:{SUPPORTED_STORES}")

    # accessing out Specific store giveaways data by key
    queried_store_key = store_name + "_giveaways"
    queried_giveaways_data = Cache.get_queried_data(store_key=queried_store_key)

    endpoint_response: dict[str, None] = API_RESPONSE_SAMPLE.copy()

    # Modifying API_RESPONSE_SAMPLE, which is {'response': None},
    endpoint_response['response'] = queried_giveaways_data
    # Making it {'response':{'queried_store_giveaways': []}} then and returning it
    return endpoint_response
