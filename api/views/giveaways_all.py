from fastapi import APIRouter
from fastapi.responses import JSONResponse

from configs.constants import ALL_GIVEAWAYS_ROUTE
from api.models.documentation_models import GiveawaysAllModel

from database.cache import Cache


router = APIRouter()


@router.get(path=ALL_GIVEAWAYS_ROUTE, response_model=GiveawaysAllModel, response_class=JSONResponse,
            tags=["giveaways"], summary="Get all ongoing giveaways")
async def get_all_giveaways() -> dict:
    return Cache.get_all_data()
