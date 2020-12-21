from ..models.repository import Repository, RepositoryInDB
from ..models.user import User, UserInDB

class CrudService:
    def save_repository(self, repository: Repository) -> None:
        raise NotImplementedError

    def get_repository_by_name(self, repository_name: str) -> RepositoryInDB:
        raise NotImplementedError

    def get_user_by_username(self, user_id: int) -> UserInDB:
        raise NotImplementedError
