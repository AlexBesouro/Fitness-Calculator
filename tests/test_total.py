import pytest

def test_total(authorized_client, test_user_data):
    res = authorized_client.post("/total")
    print(res.json())
    assert res.status_code == 200