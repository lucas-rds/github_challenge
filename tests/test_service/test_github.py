import pytest
from unittest.mock import Mock, MagicMock
from pytest_mock import MockerFixture
from app.domain.services.github import GithubService
from app.service.github import GithubFetchService


def test_github_service_interface():
    github_service = GithubService()
    with pytest.raises(NotImplementedError):
        github_service.fetch_repositories_by_username(None)

    with pytest.raises(NotImplementedError):
        github_service.fetch_repository_by_user_and_name(None, None)


def test_fetch_repositories_by_username(mocker: MockerFixture):
    github_service = GithubFetchService()

    response = Mock()
    response.raise_for_status = Mock()
    response.json.return_value = [{"repo": "repo1"}]
    mocker.patch("requests.get", return_value=response)

    repositories = github_service.fetch_repositories_by_username(None)
    assert repositories == response.json.return_value


def test_fetch_repository_by_user_and_name(mocker: MockerFixture):
    github_service = GithubFetchService()

    response = Mock()
    response.raise_for_status = Mock()
    response.json.return_value = [{"repo": "repo1"}]
    mocker.patch("requests.get", return_value=response)

    repositories = github_service.fetch_repository_by_user_and_name(None, None)
    assert repositories == response.json.return_value
