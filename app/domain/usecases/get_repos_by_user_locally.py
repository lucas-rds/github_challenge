from pydantic import BaseModel
from app.domain.models.user import UserOut
from app.domain.services.github import GithubService
from app.domain.services.crud import CrudService
from app.domain.exceptions.not_found import NotFoundError


class GetReposByUserLocallyUseCase:
    def __init__(self, crud: CrudService, username: str):
        self.crud = crud
        self.username = username

    def execute(self) -> UserOut:
        user = self.crud.get_user_by_username(self.username)
        if not user:
            raise NotFoundError
        return user
