import json


class GithubService:
    def fetch_repositories_by_username(self, username: str) -> json:
        raise NotImplementedError

    def fetch_repository_by_user_and_name(self, username: str, repository_name: str) -> json:
        raise NotImplementedError
