from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Owner(BaseModel):
    login: str
    id: int

class RepositoryBase(BaseModel):
    url: str
    name: str
    private: bool
    created_at: str
    updated_at: str
    size: int
    stargazers_count: int
    watchers_count: int

class Repository(RepositoryBase):
    owner: Optional[Owner]

class RepositoryOut(RepositoryBase):
    pass

class RepositoryInDB(RepositoryBase):
    class Config:
        orm_mode = True
