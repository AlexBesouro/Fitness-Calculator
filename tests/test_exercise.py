import pytest
from app import schemas

def test_exercise(client):
    res = client.get("/exercises")
    assert res.status_code == 200