from pydantic import BaseModel

from app.domain.models.user import UserOut
from app.domain.services.github import GithubService
from app.domain.services.crud import CrudService


class GetReposByUserRemotelyUseCase:
    def __init__(self, github_repository: GithubService, username: str):
        self.github_repository = github_repository
        self.username = username

    def execute(self) -> UserOut:
        respositories = self.github_repository.fetch_repositories_by_username(
            self.username)
        return UserOut(id=respositories[0]["owner"]["id"],
                       username=self.username,
                       repositories=respositories)
