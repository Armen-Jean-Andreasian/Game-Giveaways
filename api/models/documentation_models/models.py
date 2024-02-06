from pydantic import BaseModel
from typing import Dict, Optional, Any


class GiveawaysAllModel(BaseModel):
    """Model for /giveaways endpoint"""
    response: Optional[Any]

class GiveawaysQueried(BaseModel):
    """Model for /giveaway queried endpoint"""
    response: Optional[Any]


class ApiInfoModel(BaseModel):
    """Model for /api_info endpoint"""
    title: str
    version: str
    description: str


class ApiHomeModel(BaseModel):
    """Model for /home and / endpoints"""
    message: str
    available_routes: Dict[str, str]
