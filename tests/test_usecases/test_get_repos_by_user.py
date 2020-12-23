import pytest
from pytest_mock import MockerFixture
from app.storage.crud import Crud, CrudService
from app.service.github import GithubFetchService, GithubService
from app.domain.models.user import UserOut
from app.domain.usecases.get_repos_by_user import GetReposByUserUseCase, GetReposByUserDto


@pytest.mark.parametrize("locally_or_remotelly, class_name", [
    (False, "GetReposByUserRemotelyUseCase"),
    (True, "GetReposByUserLocallyUseCase"),
])
def test_fetch_repositories_by_username_remotelly(mocker: MockerFixture,
                                                  crud: CrudService,
                                                  github: GithubService,
                                                  locally_or_remotelly: bool,
                                                  class_name: str):
    username = 'test'
    dto = GetReposByUserDto(crud=crud,
                            github_repository=github,
                            username=username,
                            from_local=locally_or_remotelly)

    user_out = UserOut(id=1, username=username)
    mocked_execute = mocker.patch(
        f"app.domain.usecases.get_repos_by_user.{class_name}.execute", return_value=user_out)

    response = GetReposByUserUseCase(dto).execute()

    mocked_execute.assert_called()
    assert response is user_out
