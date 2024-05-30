from typing import Optional, List
from src.core.entities.grimoire import Grimoire

class InterfaceGrimoireRepository:
    def create(self, grimoire: Grimoire) -> Grimoire:
        # Lógica para crear un nuevo grimorio en la base de datos
        pass
    
    def find_by_id(self, grimoire_id: str) -> Grimoire:
        # Lógica para buscar un grimorio por su ID en la base de datos
        pass
    
    def update(self, grimoire: Grimoire) -> Grimoire:
        # Lógica para actualizar un grimorio en la base de datos
        pass
    
    def delete(self, grimoire_id: str) -> None:
        # Lógica para eliminar un grimorio de la base de datos
        pass
    def get_all(self) -> List[Grimoire]: pass