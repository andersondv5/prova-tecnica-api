#!/bin/sh
set -e

# Espera simples pelo Postgres
if [ -n "$POSTGRES_HOST" ]; then
echo "Esperando pelo banco $POSTGRES_HOST:$POSTGRES_PORT..."
until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
sleep 1
done
fi

# Cria superuser automático se ativado
if [ "$CREATE_SUPERUSER" = "1" ]; then
echo "from django.contrib.auth import get_user_model; User=get_user_model();\nif not User.objects.filter(username=\"admin\").exists():\n User.objects.create_superuser(\"admin\", \"admin@example.com\", \"admin\")" | python manage.py shell
fi


python manage.py collectstatic --noinput || true
python manage.py runserver 0.0.0.0:8000

chmod +x backend/entrypoint.sh