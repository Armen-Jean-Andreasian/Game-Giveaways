from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..models.documentation_models import GiveawaysAllModel
from configs.constants import ALL_GIVEAWAYS_DEFAULT_RESPONSE

router = APIRouter()


@router.get("/sample_data", response_model=GiveawaysAllModel, response_class=JSONResponse, tags=["sample_data"],
            summary="Get sample store_data")
async def get_sample_data() -> dict:
    """Get response sample for giveaways."""
    return ALL_GIVEAWAYS_DEFAULT_RESPONSE
