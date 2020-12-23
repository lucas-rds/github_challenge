import pytest
from pytest_mock import MockerFixture
from app.storage.crud import Crud, BaseCrud
from app.domain.models.user import UserOut
from app.domain.models.repository import RepositoryOut, Owner
from app.domain.usecases.get_repos_by_user_remotely import GetReposByUserRemotelyUseCase, BaseGithub


def test_fetch_repositories_by_username_remotelly_success(mocker: MockerFixture,
                                                          github: BaseGithub):
    repositories = [{"url": "repository.url",
                     "name": "repository.name",
                     "private": False,
                     "created_at": "repository.created_at",
                     "updated_at": "repository.updated_at",
                     "size": 1,
                     "stargazers_count": 2,
                     "watchers_count": 3,
                     "owner": {
                         "login": "login",
                         "id": 123
                     }}]
    mock = mocker.patch.object(github,
                               "fetch_repositories_by_username",
                               return_value=repositories)

    response = GetReposByUserRemotelyUseCase(github, 'test').execute()

    mock.assert_called()
    assert len(response.repositories) == 1
    assert response.username == 'test'
    assert response.id == 123


def test_fetch_repositories_by_username_remotelly_error(mocker: MockerFixture,
                                                        github: BaseGithub):
    mocker.patch.object(github,
                        "fetch_repositories_by_username",
                        side_effect=Exception)
    with pytest.raises(Exception):
        GetReposByUserRemotelyUseCase(github, 'test').execute()
