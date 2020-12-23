import pytest
from pytest_mock import MockerFixture
from app.storage.crud import Crud, CrudService
from app.service.github import GithubFetchService, GithubService
from app.domain.models.user import UserInDB
from app.domain.usecases.get_repos_by_user_locally import GetReposByUserLocallyUseCase
from app.domain.exceptions.not_found import NotFoundError


def test_GetReposByUserLocallyUseCase_execute_success(mocker: MockerFixture, crud: CrudService):
    username = 'test'
    user = UserInDB(id=1, username=username)
    mock = mocker.patch.object(crud,
                               "get_user_by_username",
                               return_value=user)

    response = GetReposByUserLocallyUseCase(crud, username).execute()

    mock.assert_called()
    assert response is user

def test_GetReposByUserLocallyUseCase_execute_error(mocker: MockerFixture, crud: CrudService):
    mock = mocker.patch.object(crud,
                               "get_user_by_username",
                               return_value=None)
    with pytest.raises(NotFoundError):
        response = GetReposByUserLocallyUseCase(crud, 'test').execute()
        mock.assert_called()
        assert response is None
