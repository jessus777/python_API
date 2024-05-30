
from sqlalchemy.orm import Session
from src.core.entities.solicitud import Solicitud
from src.core.repositories.solicitud_repository import InterfaceSolicitudRepository
from src.infraestructure.database import SessionLocal
from typing import Optional, List


class SolicitudRepository(InterfaceSolicitudRepository):
    def __init__(self, session: Session = SessionLocal):
        self.session = session

    def create(self, solicitud: Solicitud) -> Solicitud:
        try:
            self.session.add(solicitud)
            self.session.commit()
            return solicitud
        except Exception as e:
            print(f"Error al crear la solicitud: {e}")
            self.db_session.rollback()
    
    def find_by_id(self, solicitud_id: int) -> Optional[Solicitud]:
        try:
            return self.session.query(Solicitud).filter(Solicitud.id == solicitud_id).first()
        except Exception as e:
            print(f"Error al obtener la solicitud: {e}")
            self.db_session.rollback()
    
    def get_all(self) -> List[Solicitud]:
        try:
            return self.session.query(Solicitud).all()
        except Exception as e:
            print(f"Error al  obtener las solicitudes: {e}")
            self.db_session.rollback()  
    

    def update(self, solicitud: Solicitud) -> Solicitud:
        try:
            self.session.add(solicitud)
            self.session.commit()
            return solicitud
        except Exception as e:
            print(f"Error al actualizar la solicitud: {e}")
            self.db_session.rollback()   
    
    def delete(self, solicitud_id: int) -> None:
        try:
            solicitud = self.find_by_id(solicitud_id)
            if solicitud:
                self.session.delete(solicitud)
                self.session.commit()
        except Exception as e:
            print(f"Error al eliminar la solicitud: {e}")
            self.db_session.rollback()      