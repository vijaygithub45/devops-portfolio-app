from app import app

def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_products():
    client = app.test_client()

    response = client.get("/api/products")

    assert response.status_code == 200

    data = response.get_json()

    assert "products" in data
    assert len(data["products"]) == 3


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "devops-portfolio-app"
