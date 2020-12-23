from sqlalchemy.orm import Session
from app.domain.models.repository import Repository, RepositoryInDB
from app.domain.models.user import User, UserInDB
from app.domain.services.base_crud import BaseCrud

from .models import User as DatabaseUser, Repository as DatabaseRepository


class Crud(BaseCrud):
    def __init__(self, db: Session):
        self.db = db

    def save_repository(self, repository: Repository) -> None:
        """Overrides BaseCrud.save_repository()"""
        user = self._get_user_by_name(repository.owner.login)
        if not user:
            user = DatabaseUser(id=repository.owner.id,
                                username=repository.owner.login)

        repo = self._get_repository_by_name(repository.name)
        if not repo:
            repo = DatabaseRepository(
                url=repository.url,
                name=repository.name,
                private=repository.private,
                created_at=repository.created_at,
                updated_at=repository.updated_at,
                size=repository.size,
                stargazers_count=repository.stargazers_count,
                watchers_count=repository.watchers_count
            )

        user.repositories.append(repo)
        self.db.add(user)
        self.db.commit()

    def get_repository_by_name(self, repository_name: str) -> RepositoryInDB:
        repository = self._get_repository_by_name(repository_name)
        return RepositoryInDB.from_orm(repository)

    def get_user_by_username(self, username: int) -> UserInDB:
        user = self._get_user_by_name(username)
        if user:
            return UserInDB.from_orm(user)

    def _get_user_by_name(self, username: str) -> DatabaseUser:
        return self.db.query(DatabaseUser).filter_by(username=username).first()

    def _get_repository_by_name(self, name: str) -> DatabaseRepository:
        return self.db.query(DatabaseRepository).filter_by(name=name).first()
