from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from requests.exceptions import HTTPError

from app.domain.exceptions.not_found import NotFoundError
from app.domain.models.user import UserOut
from app.domain.models.repository import RepositoryOut
from app.domain.usecases.get_repos_by_user import GetReposByUserUseCase, GetReposByUserDto
from app.domain.usecases.get_repo_by_user_and_name import GetRepoByUserAndNameUseCase, GetRepoByUserAndNameDto
from app.domain.services.github import GithubService
from app.storage.crud import Crud
from .injection import create_crud, create_github_service

repository_router = APIRouter(prefix="/repositories")


@repository_router.get("/", response_model=UserOut)
def repositories_by_user(
        username: str,
        from_local: bool = False,
        crud: Crud = Depends(create_crud),
        github_repository: GithubService = Depends(create_github_service)):

    try:
        dto = GetReposByUserDto(crud=crud,
                                github_repository=github_repository,
                                username=username,
                                from_local=from_local)
        return GetReposByUserUseCase(dto).execute()
    except ConnectionError:
        raise HTTPException(status_code=503,
                            detail="Github service may be unavailable, try again later")
    except HTTPError as err:
        raise HTTPException(status_code=err.response.status_code,
                            detail=err.response.text)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="not found")


@ repository_router.get("/{repository_name}", response_model=RepositoryOut)
def repository_by_username_and_name(
        save_data: bool,
        username: str,
        repository_name: str,
        crud: Crud = Depends(create_crud),
        github_repository: GithubService = Depends(create_github_service)):

    try:
        dto = GetRepoByUserAndNameDto(**{"crud": crud,
                                         "github_repository": github_repository,
                                         "username": username,
                                         "repository_name": repository_name,
                                         "save_data": save_data})

        return GetRepoByUserAndNameUseCase(dto).execute()
    except ConnectionError:
        raise HTTPException(status_code=503,
                            detail="Github service may be unavailable, try again later")
    except HTTPError as err:
        raise HTTPException(status_code=err.response.status_code,
                            detail=err.response.text)


router = APIRouter()
router.include_router(repository_router)


@ router.get("/")
def health():
    return "OK"
