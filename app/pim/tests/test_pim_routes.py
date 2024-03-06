from fastapi.testclient import TestClient

from app import app

uts_api_client = TestClient(app=app)


def test_should_return_status_200_when_get_request_hello_world():
    response = uts_api_client.get("/pim")

    assert response.status_code == 200
    assert response.json() == {"response": "Hello world"}
