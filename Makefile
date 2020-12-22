
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

create-migration:
	alembic revision --autogenerate -m "$(shell date '+%Y-%m-%d %H:%M:%S')"

migrate:
	alembic upgrade head