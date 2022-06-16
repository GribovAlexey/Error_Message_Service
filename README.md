Project deployment steps:
1) Download project files.
2) Set up venv.
3) Run "pip install -r requirements.txt".
4) Create database.
5) Set up local .env accordingly to .env.example file.
6) Run "python manage.py collectstatic".
7) Set up source "message_app/.env" and run Celery by "celery -A my_celery worker --loglevel=INFO" for message sending.
8) Set up source "message_app/.env" and run project by "python manage.py runserver".