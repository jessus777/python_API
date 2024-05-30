from sqlalchemy.orm import Session
from src.core.entities.grimoire import Grimoire
from src.core.repositories.grimoire_repository import InterfaceGrimoireRepository
from typing import List

class GrimoireUsesCase:
    def __init__(self, grimoire_repository: InterfaceGrimoireRepository):
        self.grimoire_repository = grimoire_repository
    
    def get_grimoires_all(self, db: Session) -> List[Grimoire]:
        try:
            grimoires = self.grimoire_repository.get_all()
            return grimoires
        except Exception as e:
            print(f"Error al obtener los grimorios: {e}")
            return []
