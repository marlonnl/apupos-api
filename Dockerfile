# Estágio 1: build da aplicação
FROM python:3.10-slim as builder

WORKDIR /app

# Copia e instala dependências
COPY Pipfile Pipfile.lock ./
# RUN pip install pipenv && pipenv install --deploy --ignore-pipfile
RUN pip install pipenv && pipenv sync

# Copia o código-fonte
COPY . .

# Etapa final: menor imagem para rodar
FROM python:3.10-slim

WORKDIR /app

# Copia somente dependências instaladas
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . .

# Variáveis para melhorar o comportamento Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expõe porta padrão do Django
EXPOSE 8000

# Comando de inicialização
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "apupos_api.wsgi:application"]