#!/bin/sh

# Executa as migrações do banco de dados
poetry run alembic upgrade head

# Inicia a aplicação
poetry run uvicorn fast_zero/app.py --host 0.0.0.0 --port 8000 --proxy-headers