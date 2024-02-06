from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..models.documentation_models import ApiHomeModel
from configs.constants import HOMEPAGE_RESPONSE, HOMEPAGE_ROUTE_V1, HOMEPAGE_ROUTE_V2


router = APIRouter()


@router.get(path=HOMEPAGE_ROUTE_V1, response_model=ApiHomeModel, response_class=JSONResponse,
            tags=["sample_data"], summary="Get the summary of the API functionalities")
@router.get(path=HOMEPAGE_ROUTE_V2, response_model=ApiHomeModel, response_class=JSONResponse,
            tags=["sample_data"], summary="Get the summary of the API functionalities")
async def get_home() -> dict:
    """Returns a summary of the API functionalities."""
    return HOMEPAGE_RESPONSE
