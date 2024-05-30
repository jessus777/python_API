from sqlalchemy.orm import Session
from src.core.entities.grimoire import Grimoire
from src.core.repositories.grimoire_repository import InterfaceGrimoireRepository
from src.infraestructure.database import SessionLocal
from typing import Optional, List

class GrimoireRepository(InterfaceGrimoireRepository):
    def __init__(self, session: Session = SessionLocal):
        self.session = session

    def _handle_error(self, operation: str, error: Exception) -> None:
        print(f"Error al {operation}: {error}")
        self.session.rollback()

    def create(self, grimoire: Grimoire) -> Optional[Grimoire]:
        try:
            self.session.add(grimoire)
            self.session.commit()
            return grimoire
        except Exception as e:
            self._handle_error("crear el grimorio", e)
            return None
    
    def find_by_id(self, grimoire_id: str) -> Optional[Grimoire]:
        try:
            return self.session.query(Grimoire).filter(Grimoire.id == grimoire_id).first()
        except Exception as e:
            self._handle_error("obtener el grimorio por ID", e)
            return None
    
    def get_all(self) -> List[Grimoire]:
        try:
            return self.session.query(Grimoire).all()
        except Exception as e:
            self._handle_error("obtener todos los grimorios", e)
            return []

    def update(self, grimoire: Grimoire) -> Optional[Grimoire]:
        try:
            self.session.add(grimoire)
            self.session.commit()
            return grimoire
        except Exception as e:
            self._handle_error("actualizar el grimorio", e)
            return None
    
    def delete(self, grimoire_id: str) -> None:
        try:
            grimoire = self.find_by_id(grimoire_id)
            if grimoire:
                self.session.delete(grimoire)
                self.session.commit()
        except Exception as e:
            self._handle_error("eliminar el grimorio", e)
