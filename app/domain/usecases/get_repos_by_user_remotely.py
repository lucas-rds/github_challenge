from app.domain.models.user import UserOut
from app.domain.services.github import GithubService
from app.domain.services.crud import CrudService


class GetReposByUserRemotelyUseCase:
    def __init__(self, github: GithubService, username: str):
        self.github = github
        self.username = username

    def execute(self) -> UserOut:
        respositories = self.github.fetch_repositories_by_username(
            self.username)
        return UserOut(id=respositories[0]["owner"]["id"],
                       username=self.username,
                       repositories=respositories)
