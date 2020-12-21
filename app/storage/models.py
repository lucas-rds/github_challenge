from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=False)
    username = Column(String(80), unique=True, nullable=False)


class Repository(Base):
    __tablename__ = "repositories"

    url = Column(Text, nullable=False, unique=True)
    name = Column(String(200), primary_key=True, autoincrement=False)
    private = Column(Boolean, default=False, nullable=False)
    created_at = Column(String(80), nullable=False)
    updated_at = Column(String(80), nullable=False)
    size = Column(String(100), nullable=False)
    stargazers_count = Column(String(100), nullable=False)
    watchers_count = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="repositories")
