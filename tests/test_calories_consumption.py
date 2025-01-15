import pytest

def test_calories_consumption(authorized_client, test_user, test_user_data):
    res = authorized_client.post("/bc", json={"exercise_name": "running 10km/h", "exercise_time": 150})
    assert res.status_code == 200