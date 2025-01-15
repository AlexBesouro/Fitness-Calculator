import pytest

def test_burned_calories(authorized_client, test_user, test_user_data):
    res = authorized_client.post("/bc", json={"exercise_name": "running 10km/h", "exercise_time": 150})
    # print(res.json())
    assert res.status_code == 200


@pytest.mark.parametrize("exercise_name, exercise_time, status_code", [("running 110km/h", 150, 404),
                                                                       ("running 10km/h", '15 min', 422),
                                                                       ("running 10km/h", None, 422),
                                                                       (None, 150, 422)])
def test_failed_burned_calories(authorized_client, test_user_data, exercise_name, exercise_time, status_code):
    data = {}
    if exercise_name is not None:
        data["exercise_name"] = exercise_name
    if exercise_time is not None:
        data["exercise_time"] = exercise_time
    res = authorized_client.post("/bc", json=data)

    assert res.status_code == status_code