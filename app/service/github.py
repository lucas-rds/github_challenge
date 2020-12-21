
import requests
import json

from app.config import GITHUB_URL
from app.domain.services.github import GithubService

class GithubFetchService(GithubService):
    def fetch_repositories_by_username(self, username: str) -> json:
        response = requests.get(f"{GITHUB_URL}/users/{username}/repos")
        response.raise_for_status()
        return response.json()

    def fetch_repository_by_user_and_name(self, username: str, repository_name: str) -> json:
        response = requests.get(f"{GITHUB_URL}/repos/{username}/{repository_name}")
        response.raise_for_status()
        return response.json()


