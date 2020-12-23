import abc
from ..models.repository import Repository, RepositoryInDB
from ..models.user import User, UserInDB

class BaseCrud(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_repository(self, repository: Repository) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_repository_by_name(self, repository_name: str) -> RepositoryInDB:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_username(self, username: int) -> UserInDB:
        raise NotImplementedError
