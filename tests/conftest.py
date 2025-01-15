import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db
from app.models import Base, Exercises
from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = (f"postgresql://{settings.database_username}:{settings.database_password}@"
                           f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

test_session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

@pytest.fixture
def session():
    print("session runs")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    running = Exercises(exercise_id=1, exercise_name="running 10km/h", exercise_met=9)
    db = test_session_local()
    db.add(running)
    db.commit()
    try:
        yield db
    finally:
        db.close()
@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


@pytest.fixture
def test_user(client):
    print("test user runs")
    user_data = {"email": "email@gmail.com",
                 "password": "password",
                 "first_name": "Alex",
                 "last_name": "Bla",
                 "user_birthday": "1996-02-05",
                 "gender": "male"}

    res = client.post("/users", json=user_data)
    new_test_user = res.json()
    new_test_user["password"] = user_data["password"]
    return new_test_user


@pytest.fixture
def access_token(test_user):
    return create_access_token({"user_id": test_user["user_id"]})

@pytest.fixture
def authorized_client(client, access_token):
    client.headers = {**client.headers, "authorization": f"bearer {access_token}"}
    return client


@pytest.fixture
def test_user_data(authorized_client, test_user):
    print("test user data runs")
    user_data = {"user_height": 180,
                 "user_weight": 80,
                 "user_activity_level": 3}

    res = authorized_client.post("/users/data", json=user_data)
    return res

@pytest.fixture
def test_food_data(client, test_user):
    print("test food data runs")
    user_data = {"food_name": "dry rice", "food_calories_100gr": 360}
    res = client.post("/food", json=user_data)
    return res

