from sqlalchemy import Column, Integer, String
from src.infraestructure.database import Base
import uuid
class Grimoire(Base):
    __tablename__ = "grimoires"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False) 