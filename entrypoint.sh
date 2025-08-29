#!/bin/sh

# Saia imediatamente se algum comando falhar
set -e

# Aguarda o banco de dados estar pronto
echo "Aguardando o banco de dados estar disponível..."
until nc -z db 5432; do
  sleep 1
done

echo "Banco de dados pronto!"

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Aplica as migrações
python manage.py migrate

# Inicia o gunicorn
exec gunicorn API.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3
