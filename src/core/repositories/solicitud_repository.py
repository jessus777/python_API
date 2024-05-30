from typing import Optional, List
from src.core.entities.solicitud import Solicitud

class InterfaceSolicitudRepository:
    def create(self, solicitud: Solicitud) -> Solicitud:
        # Lógica para crear una nueva solicitud en la base de datos
        pass
    
    def find_by_id(self, solicitud_id: int) -> Solicitud:
        # Lógica para buscar una solicitud por su ID en la base de datos
        pass
    
    def update(self, solicitud: Solicitud) -> Solicitud:
        # Lógica para actualizar una solicitud en la base de datos
        pass
    
    def delete(self, solicitud_id: int) -> None:
        # Lógica para eliminar una solicitud de la base de datos
        pass
    
    def get_all(self) -> List[Solicitud]: pass