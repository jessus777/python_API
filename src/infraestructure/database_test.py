
from sqlalchemy import text
from infraestructure.database import get_db, engine

def test_database_connection():
    connection = engine.connect()
    assert connection is not None
    connection.close()

def test_session_creation():
    with next(get_db()) as db:
        assert db is not None

def test_execute_query():
    with next(get_db()) as db:
        result = db.execute(text("SELECT 1"))
        assert result.scalar() == 1