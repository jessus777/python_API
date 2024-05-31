from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.repositories.grimoire_repository import InterfaceGrimoireRepository
from src.core.uses_case.grimoire_use_case import GrimoireUsesCase
from src.infraestructure.database import get_db


grimoire_route = APIRouter()


@grimoire_route.get("/grimoires")
async def list_grimoires(db: Session = Depends(get_db)):
    try:
        grimoire_repository = InterfaceGrimoireRepository()
        grimoire_use_case = GrimoireUsesCase(grimoire_repository)
        grimoires = grimoire_use_case.get_grimoires_all(db)
        return {
            "message": "lista de grimorios",
            "grimoires": grimoires
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))