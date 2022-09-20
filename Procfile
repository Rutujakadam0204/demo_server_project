web: quotes.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A quotes.celery worker -l info