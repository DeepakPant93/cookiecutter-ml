from starlette.testclient import TestClient
from {{cookiecutter.project_slug}}.main import app

client = TestClient(app=app)

def test_train_model():
    response = client.post("/api/v1/train-model")
    assert response.status_code == 200
    assert response.json() is not None


def test_predict():
    response = client.post("/api/v1/predict")
    assert response.status_code == 200
    assert response.json() is not None
