web: gunicorn keyboarding_games.wsgi

release: python manage.py collectstatic && python manage.py migrate --noinput
