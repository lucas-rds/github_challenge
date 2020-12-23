import pytest
from pytest_mock import MockerFixture
from app.storage.crud import Crud, BaseCrud
from app.service.github import Github, BaseGithub
from app.domain.models.user import UserOut
from app.domain.usecases.get_repo_by_user_and_name import GetRepoByUserAndNameUseCase, GetRepoByUserAndNameDto

repository = {"url": "repository.url",
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
              }}


def test_GetRepoByUserAndNameUseCase_execute(mocker: MockerFixture,
                                             crud: BaseCrud,
                                             github: BaseGithub):
    dto = GetRepoByUserAndNameDto(crud=crud,
                                  github_repository=github,
                                  username='test',
                                  repository_name='test',
                                  save_data=False)

    fetch_mock = mocker.patch.object(github,
                                     "fetch_repository_by_user_and_name",
                                     return_value=repository)

    GetRepoByUserAndNameUseCase(dto).execute()

    fetch_mock.assert_called()


def test_GetRepoByUserAndNameUseCase_execute_save_data(mocker: MockerFixture,
                                                       crud: BaseCrud,
                                                       github: BaseGithub):
    dto = GetRepoByUserAndNameDto(crud=crud,
                                  github_repository=github,
                                  username='test',
                                  repository_name='test',
                                  save_data=True)

    fetch_repo_mock = mocker.patch.object(github,
                                     "fetch_repository_by_user_and_name",
                                     return_value=repository)
    save_repository_mock = mocker.patch.object(crud, "save_repository")
    get_repository_by_name_mock = mocker.patch.object(crud,
                                         "get_repository_by_name",
                                         return_value=repository)

    GetRepoByUserAndNameUseCase(dto).execute()

    fetch_repo_mock.assert_called()
    save_repository_mock.assert_called()
    get_repository_by_name_mock.assert_called()
