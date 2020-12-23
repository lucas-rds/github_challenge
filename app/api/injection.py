from fastapi import Depends
from sqlalchemy.orm import Session

from app.service.github import Github
from app.storage.crud import Crud
from app.storage.database import CreateSession

from app.domain.services.base_crud import BaseCrud
from app.domain.services.base_github import BaseGithub

def create_session() -> Session:
    db = CreateSession()
    try:
        yield db
    finally:
        db.close()


def create_crud(db: Session = Depends(create_session)) -> BaseCrud:
    return Crud(db)


def create_github_service() -> BaseGithub:
    return Github()
