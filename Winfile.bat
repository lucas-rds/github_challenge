echo off
set arg=%1

echo %arg%

if %arg%==run (uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload)

if %arg%==create-migration (alembic revision --autogenerate -m "%date%%time%")

if %arg%==migrate (alembic upgrade head)

if %arg%==test (pytest -v --cov-report term-missing --cov-report html:coverage --cov app/)