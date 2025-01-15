from http.client import responses
import pytest
from app import schemas

def test_root(client):
    response = client.get("/")
    assert response.json().get("data") == "Fitness Calculator"
    assert response.status_code == 200
# ----------------------------------------------------------------------------------------------------------------------

def test_create_user(client):
    res = client.post("/users", json={"email": "email@gmail.com",
                                      "password": "password",
                                      "first_name": "Alex",
                                      "last_name": "Bla",
                                      "user_birthday": "1996-02-05",
                                      "gender": "male"})
    new_user_res = schemas.UserResponse(**res.json())
    assert new_user_res.email == "email@gmail.com"
    assert res.status_code == 201
# ----------------------------------------------------------------------------------------------------------------------


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    assert res.status_code == 200




@pytest.mark.parametrize("email, password, status_code", [("email", "wrong password", 403),
                                                          ("wrong email", "password", 403),
                                                          ("wrong email", "wrong password", 403),
                                                          (None, "password", 422),
                                                          ("email", None, 422)])
def test_failed_login(test_user, client, email, password, status_code):
    data = {}
    if email is not None:
        data["username"] = email
    if password is not None:
        data["password"] = password
    res = client.post("/login", data=data)
    assert res.status_code == status_code
    # assert res.json().get("detail") == "Invalid credentials"1
# ----------------------------------------------------------------------------------------------------------------------


def test_create_user_data(authorized_client):
    res = authorized_client.post("/users/data", json={"user_height": 180,
                                                      "user_weight": 80,
                                                      "user_activity_level": 3})
    assert res.status_code == 201


@pytest.mark.parametrize("user_height, user_weight, user_activity_level, status_code", [(180, 80, 6, 422),
                                                                                        (180, 80, 0, 422),
                                                                                        (180, 800, 5, 422),
                                                                                        (180, 10, 3, 422),
                                                                                        (1080, 80, 2, 422),
                                                                                        (20, 80, 2, 422),
                                                                                        (None, 80, 2, 422),
                                                                                        (120, None, 2, 422),
                                                                                        (120, 80, None, 422)])
def test_failed_create_user_data(test_user, client, user_height, user_weight, user_activity_level, status_code):
    data = {}
    if user_height is not None:
        data["user_height"] = user_height
    if user_weight is not None:
        data["user_weight"] = user_weight
    if user_activity_level is not None:
        data["user_activity_level"] = user_activity_level
    res = client.post("/login", data=data)
    assert res.status_code == status_code
#----------------------------------------------------------------------------------------------------------------------


def test_find_user(client, test_user):
    res = client.get(f"/users/{test_user["user_id"]}")
    assert res.status_code == 200

def test_failed_find_user(client):
    res = client.get("/users/2")
    assert res.status_code == 404