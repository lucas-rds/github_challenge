from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from .repository import RepositoryOut, RepositoryInDB


class User(BaseModel):
    id: int
    username: str
    repositories: List[RepositoryOut] = []


class UserOut(User):
    pass


class UserInDB(User):
    repositories: List[RepositoryInDB] = []

    class Config:
        orm_mode = True
