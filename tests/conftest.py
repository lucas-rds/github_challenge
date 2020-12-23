import pytest

from unittest.mock import Mock, MagicMock
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.storage.crud import Crud, CrudService
from app.service.github import GithubFetchService, GithubService
from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def db() -> Mock:
    mock = Mock()
    mock.add = MagicMock()
    mock.commit = MagicMock()
    mock.query = MagicMock(return_value=MagicMock())
    mock.query.filter_by = MagicMock(return_value=MagicMock())
    mock.query.filter_by.first = MagicMock(return_value=MagicMock())
    return mock


@pytest.fixture
def crud(db: Mock) -> CrudService:
    return Crud(db)

@pytest.fixture
def github() -> GithubService:
    return GithubFetchService()
