import pytest
from sqlalchemy.orm import sessionmaker
from src.infraestructure.database import engine, Base
from src.infraestructure.repositories.grimoire_repository import GrimoireRepository

@pytest.fixture(scope="session")
def setup_database():
    # Crear todas las tablas en la base de datos
    Base.metadata.create_all(bind=engine)

    # Permitir que las pruebas se ejecuten
    yield


@pytest.fixture
def session():
    # Configurar una sesión de base de datos para las pruebas
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Permitir que las pruebas se ejecuten
    yield session
    
    # Cerrar la sesión después de que las pruebas se completen
    session.close()

def test_get_all(session, setup_database):
    # Crear el repositorio con la sesión de la base de datos
    repository = GrimoireRepository(session=session)

    # Llamar al método get_all
    result = repository.get_all()
   
   
    # Verificar los atributos de cada objeto Grimoire en la lista
    for grimoire in result:
        print(f"Grimoire ID: {grimoire.id}, Name: {grimoire.name}, Level: {grimoire.level}")
    
    # Verificar que la lista resultante no esté vacía
    assert result
    # Verificar que se obtuvieron los resultados esperados
# Verificar que inicialmente no hay ningún grimoire en la base de datos
