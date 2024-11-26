from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Using pydantic for managing settings via environment variables using the BaseSettings class.
# Providing url for connection to my DB
SQLALCHEMY_DATABASE_URL = (f"postgresql://{settings.database_username}:{settings.database_password}@"
                           f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}")

# Engine create a connection to DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sesionmaker is a factory class for creating a Session object which is an interface for interacting with the database.
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)


# get_db function:
# Creates a session.
# Yields the session connection to the calling code.
# Ensures the session is properly closed after use (via a context manager or try/finally).

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

