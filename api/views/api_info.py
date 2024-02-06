from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.models.documentation_models import ApiInfoModel
from configs.constants import API_NAME, API_VERSION, API_DESCRIPTION, API_INFO_ROUTE

ENDPOINT_RESPONSE: dict = {"title": API_NAME, "version": API_VERSION, "description": API_DESCRIPTION, }

router = APIRouter()


@router.get(path=API_INFO_ROUTE, response_model=ApiInfoModel, response_class=JSONResponse, tags=["api_info"],
            summary="Get a dictionary containing information about the API")
async def get_api_info() -> dict:
    """Returns a dictionary containing information about the API"""
    return ENDPOINT_RESPONSE
