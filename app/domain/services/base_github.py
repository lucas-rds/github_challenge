import abc
import json

class BaseGithub(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_repositories_by_username(self, username: str) -> json:
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_repository_by_user_and_name(self, username: str, repository_name: str) -> json:
        raise NotImplementedError
