from app.domain.models.user import UserOut
from app.domain.services.base_github import BaseGithub
from app.domain.services.base_crud import BaseCrud


class GetReposByUserRemotelyUseCase:
    def __init__(self, github: BaseGithub, username: str):
        self.github = github
        self.username = username

    def execute(self) -> UserOut:
        respositories = self.github.fetch_repositories_by_username(
            self.username)
        return UserOut(id=respositories[0]["owner"]["id"],
                       username=self.username,
                       repositories=respositories)
