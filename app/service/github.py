
import requests
import json

from app.config import GITHUB_URL
from app.domain.services.base_github import BaseGithub


class Github(BaseGithub):
    def fetch_repositories_by_username(self, username: str) -> json:
        """Overrides BaseGithub.fetch_repositories_by_username()"""
        response = requests.get(f"{GITHUB_URL}/users/{username}/repos")
        response.raise_for_status()
        return response.json()

    def fetch_repository_by_user_and_name(self, username: str, repository_name: str) -> json:
        """Overrides BaseGithub.fetch_repository_by_user_and_name()"""
        response = requests.get(
            f"{GITHUB_URL}/repos/{username}/{repository_name}")
        response.raise_for_status()
        return response.json()
