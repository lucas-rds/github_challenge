from fastapi import Depends
from sqlalchemy.orm import Session

from app.service.github import GithubFetchService
from app.storage.crud import Crud
from app.storage.database import CreateSession

from app.domain.services.crud import CrudService
from app.domain.services.github import GithubService

def create_session() -> Session:
    db = CreateSession()
    try:
        yield db
    finally:
        db.close()


def create_crud(db: Session = Depends(create_session)) -> CrudService:
    return Crud(db)


def create_github_service() -> GithubService:
    return GithubFetchService()
