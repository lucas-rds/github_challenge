from pydantic import BaseModel

from app.domain.models.user import UserOut
from app.domain.services.github import GithubService
from app.domain.services.crud import CrudService
from .get_repos_by_user_locally import GetReposByUserLocallyUseCase
from .get_repos_by_user_remotely import GetReposByUserRemotelyUseCase


class GetReposByUserDto(BaseModel):
    crud: CrudService
    github_repository: GithubService
    username: str
    from_local: bool

    class Config:
        arbitrary_types_allowed = True


class GetReposByUserUseCase:
    def __init__(self, dto: GetReposByUserDto):
        self.crud = dto.crud
        self.github_repository = dto.github_repository
        self.username = dto.username
        self.from_local = dto.from_local

    def execute(self) -> UserOut:
        if self.from_local:
            return GetReposByUserLocallyUseCase(self.crud, self.username).execute()
        return GetReposByUserRemotelyUseCase(self.github_repository, self.username).execute()
