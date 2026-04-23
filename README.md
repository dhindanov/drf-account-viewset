uv run python manage.py runserver 127.0.0.1:7000 --settings=server.settings
uv run uvicorn server.asgi:application --reload --port 7000
