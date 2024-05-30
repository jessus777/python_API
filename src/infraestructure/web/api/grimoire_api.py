from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.uses_case.grimoire_use_case import GrimoireUsesCase

grimoire_route = APIRouter()
grimoire_use_case = GrimoireUsesCase()

async def get_all_grimoires():
    try:
        grimoires = grimoire_use_case.get_grimoires_all()
        return {
            "message": "lista de grimores",
             "grimoires": [grimoire.dict() for grimoire in grimoires]
        }
    except Exception as e:
        raise  HTTPException(status_code=400, detail=str(e))
    
@grimoire_route.get("/grimoires")
async def list_grimoires():
    return await get_all_grimoires()