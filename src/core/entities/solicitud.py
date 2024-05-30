from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infraestructure.database import Base

class Solicitud(Base):
    __tablename__ = "solicitud"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    identificacion = Column(String(20), nullable=False)
    edad = Column(Integer, nullable=False)
    afinidad_magica = Column(String(20), nullable=False)
    grimoire_id = Column(String, ForeignKey('grimoires.id'), nullable=False)

    grimoire = relationship("Grimoire")