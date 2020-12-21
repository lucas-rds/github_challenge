
run:
	uvicorn app.main:app --reload

create-migration:
	alembic revision --autogenerate -m "$(shell date '+%Y-%m-%d %H:%M:%S')"

migrate:
	alembic upgrade head