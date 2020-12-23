import pytest

from unittest.mock import Mock, MagicMock
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.storage.crud import Crud, BaseCrud
from app.service.github import Github, BaseGithub
from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def db() -> Mock:
    return Mock()


@pytest.fixture
def crud(db: Mock) -> BaseCrud:
    return Crud(db)

@pytest.fixture
def github() -> BaseGithub:
    return Github()
