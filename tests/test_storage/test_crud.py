import pytest
from unittest.mock import Mock, MagicMock
from pytest_mock import MockerFixture

from app.storage.crud import Crud
from app.storage.models import User as DatabaseUser, Repository as DatabaseRepository
from app.domain.models.repository import Repository, RepositoryInDB, Owner

from app.domain.services.crud import CrudService


def test_crud_service_interface():
    crud_service = CrudService()
    with pytest.raises(NotImplementedError):
        crud_service.save_repository(None)

    with pytest.raises(NotImplementedError):
        crud_service.get_repository_by_name(None)

    with pytest.raises(NotImplementedError):
        crud_service.get_user_by_username(None)


def test_save_repository_with_valid_repo_and_user(mocker: MockerFixture, db: Mock):
    crud = Crud(db)
    _get_user_by_name_mock = mocker.patch.object(crud, '_get_user_by_name')
    _get_repository_by_name_mock = mocker.patch.object(
        crud, '_get_repository_by_name')

    repository = Repository(
        url="repository.url",
        name="repository.name",
        private=False,
        created_at="repository.created_at",
        updated_at="repository.updated_at",
        size=1,
        stargazers_count=2,
        watchers_count=3,
        owner=Owner(
            login="login",
            id=1
        )
    )

    crud.save_repository(repository)

    _get_user_by_name_mock.assert_called()
    _get_repository_by_name_mock.assert_called()
    db.add.assert_called()
    db.commit.assert_called()


def test_save_repository_with_none_repo_and_user(mocker: MockerFixture, db: Mock):
    crud = Crud(db)
    _get_user_by_name_mock = mocker.patch.object(
        crud, '_get_user_by_name', return_value=None)
    _get_repository_by_name_mock = mocker.patch.object(
        crud, '_get_repository_by_name', return_value=None)

    repository = Repository(
        url="repository.url",
        name="repository.name",
        private=False,
        created_at="repository.created_at",
        updated_at="repository.updated_at",
        size=1,
        stargazers_count=2,
        watchers_count=3,
        owner=Owner(
            login="login",
            id=1
        )
    )

    crud.save_repository(repository)

    _get_user_by_name_mock.assert_called()
    _get_repository_by_name_mock.assert_called()
    db.add.assert_called()
    db.commit.assert_called()


def test_get_repository_by_name(mocker: MockerFixture, db: Mock):
    repo = DatabaseRepository(
        url="repository.url",
        name="repository.name",
        private=False,
        created_at="repository.created_at",
        updated_at="repository.updated_at",
        size=1,
        stargazers_count=2,
        watchers_count=3
    )
    db.query().filter_by().first.return_value = repo
    crud = Crud(db)
    repository = crud.get_repository_by_name("test")

    assert repository is not None
    assert repository.url == repo.url
    assert repository.name == repo.name


def test_get_user_by_username_success(mocker: MockerFixture, db: Mock):
    user = DatabaseUser(id=1, username="test")
    db.query().filter_by().first.return_value = user
    crud = Crud(db)
    user_response = crud.get_user_by_username("test")

    assert user_response is not None
    assert user_response.id == user.id
    assert user_response.username == user.username


def test_get_user_by_username_fail(mocker: MockerFixture, db: Mock):
    db.query().filter_by().first.return_value = None
    crud = Crud(db)
    user_response = crud.get_user_by_username("test")

    assert user_response is None
