import pytest

def test_food(authorized_client):
    res = authorized_client.post("/food", json={"food_name": "dry rice", "food_calories_100gr": 360})
    assert res.status_code == 201

@pytest.mark.parametrize("food_name, food_calories_100gr, status_code", [("dry rice", 360, 409),
                                                                       ("dry rice", None, 422),
                                                                       (None, 360, 422)])
def test_failed_food(authorized_client, test_food_data, food_name, food_calories_100gr, status_code):
    data = {}
    if food_name is not None:
        data["food_name"] = food_name
    if food_calories_100gr is not None:
        data["food_calories_100gr"] = food_calories_100gr
    res = authorized_client.post("/food", json=data)
    assert res.status_code == status_code