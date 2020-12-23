import pytest
from unittest.mock import Mock, MagicMock
from pytest_mock import MockerFixture
from app.domain.services.base_github import BaseGithub
from app.service.github import Github

def test_github_service_interface_validation():
    with pytest.raises(TypeError):
        BaseGithub()

def test_github_service_interface_raises(mocker: MockerFixture):
    mocker.patch.object(BaseGithub, "__abstractmethods__", new_callable = set)
    github_service = BaseGithub()
    with pytest.raises(NotImplementedError):
        github_service.fetch_repositories_by_username(None)

    with pytest.raises(NotImplementedError):
        github_service.fetch_repository_by_user_and_name(None, None)


def test_fetch_repositories_by_username(mocker: MockerFixture):
    github_service = Github()

    expected = [{"repo": "repo1"}]
    response = Mock()
    response.json.return_value = expected
    mocker.patch("requests.get", return_value=response)

    repositories = github_service.fetch_repositories_by_username(None)
    assert repositories == expected


def test_fetch_repository_by_user_and_name(mocker: MockerFixture):
    github_service = Github()

    expected = [{"repo": "repo1"}]
    response = Mock()
    response.json.return_value = expected
    mocker.patch("requests.get", return_value=response)

    repositories = github_service.fetch_repository_by_user_and_name(None, None)
    assert repositories == expected
