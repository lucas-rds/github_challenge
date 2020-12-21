from app.domain.models.repository import RepositoryOut, Repository
from app.domain.services.github import GithubService
from app.domain.services.crud import CrudService
from pydantic import BaseModel


class GetRepoByUserAndNameDto(BaseModel):
    crud: CrudService
    github_repository: GithubService
    username: str
    repository_name: str
    save_data: bool

    class Config:
        arbitrary_types_allowed = True


class GetRepoByUserAndNameUseCase:
    def __init__(self, dto: GetRepoByUserAndNameDto):
        self.crud = dto.crud
        self.github_repository = dto.github_repository
        self.username = dto.username
        self.repository_name = dto.repository_name
        self.save_data = dto.save_data

    def execute(self) -> RepositoryOut:
        repository = self.github_repository.fetch_repository_by_user_and_name(
            self.username,
            self.repository_name)

        if self.save_data:
            self.crud.save_repository(Repository.parse_obj(repository))
            repository = self.crud.get_repository_by_name(self.repository_name)

        return RepositoryOut.parse_obj(repository)
