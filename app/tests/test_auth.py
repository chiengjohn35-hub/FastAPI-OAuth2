import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.main import app
from app.database import Base, get_db




# ---- Test Database ----
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# ---- Dependency Override ----
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register",
        json={"name": "John Doe", "email": "try@example.com", "password": "123456"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "try@example.com"
    assert data["name"] == "John Doe"
    assert "id" in data



def test_login_user():
    # First register
    client.post(
        "/auth/register",
        json={"name": "John Doe", "email": "login@example.com", "password": "123456"}
    )

    # Then login
    response = client.post(
        "/auth/token",
        data={"username": "login@example.com", "password": "123456"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_me_endpoint():
    # Register
    client.post(
        "/auth/register",
        json={"name": "John Doe", "email": "me@example.com", "password": "123456"}
    )

    # Login
    login = client.post(
        "/auth/token",
        data={"username": "me@example.com", "password": "123456"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    token = login.json()["access_token"]

    # Call /auth/me
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "me@example.com"
    assert data["name"] == "John Doe"
