import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture
from requests.exceptions import HTTPError
from requests import Response
from app.domain.models.user import UserOut
from app.domain.models.repository import RepositoryOut
from app.domain.exceptions.not_found import NotFoundError


def test_home(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_repositories_by_user_success(mocker: MockerFixture, client: TestClient):
    user_out = UserOut(id=1, username="test")
    mocker.patch('app.api.router.GetReposByUserUseCase.execute', return_value=user_out)
    response = client.get("/repositories/?username=test&from_local=true")
    assert response.status_code == 200
    assert response.json() == user_out.dict()


def test_repositories_by_user_required_params(mocker: MockerFixture, client: TestClient):
    response = client.get("/repositories/")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['query', 'username'],
                                           'msg': 'field required',
                                           'type': 'value_error.missing'}]}


http_error_response_mock = Response()
http_error_response_mock._content = b'github error'
http_error_response_mock.status_code = 400


@pytest.mark.parametrize("err, expected_status_code, expected_response", [
    (ConnectionError(), 503, {
     'detail': 'Github service may be unavailable, try again later'}),
    (HTTPError(response=http_error_response_mock),
     http_error_response_mock.status_code,
     {"detail": http_error_response_mock._content.decode("utf-8")}),
    (NotFoundError, 404, {"detail": "not found"}),
])
def test_repositories_by_user_fail(mocker: MockerFixture,
                                   client: TestClient,
                                   err: Exception,
                                   expected_status_code: int,
                                   expected_response: dict):

    mocker.patch('app.api.router.GetReposByUserUseCase.execute',
                 side_effect=err)
    response = client.get("/repositories/?username=test&from_local=true")
    assert response.status_code == expected_status_code
    assert response.json() == expected_response


def test_repository_by_username_and_name_success(mocker: MockerFixture, client: TestClient):
    repo_out = RepositoryOut(url="url_test",
                             name="name_test",
                             private=False,
                             created_at="2018-10-29T10:29:02Z",
                             updated_at="2018-10-29T10:29:02Z",
                             size=1,
                             stargazers_count=1,
                             watchers_count=1)

    mocker.patch(
        'app.api.router.GetRepoByUserAndNameUseCase.execute', return_value=repo_out)
    response = client.get("/repositories/repo_name_test/?username=test&save_data=true")
    assert response.status_code == 200
    assert response.json() == repo_out.dict()


@pytest.mark.parametrize("err, expected_status_code, expected_response", [
    (ConnectionError(), 503, {
     'detail': 'Github service may be unavailable, try again later'}),
    (HTTPError(response=http_error_response_mock),
     http_error_response_mock.status_code,
     {"detail": http_error_response_mock._content.decode("utf-8")})
])
def test_repository_by_username_and_name_fail(mocker: MockerFixture,
                                              client: TestClient,
                                              err: Exception,
                                              expected_status_code: int,
                                              expected_response: dict):

    mocker.patch(
        'app.api.router.GetRepoByUserAndNameUseCase.execute',
        side_effect=err)
    response = client.get("/repositories/repo_name_test/?username=test&save_data=true")
    assert response.status_code == expected_status_code
    assert response.json() == expected_response
