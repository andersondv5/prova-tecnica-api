FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copia os arquivos de requisitos primeiro para otimizar o cache do Docker
COPY requirements.txt .

RUN apt-get update \
&& apt-get install -y build-essential libpq-dev gcc git netcat --no-install-recommends \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& apt-get remove -y build-essential gcc git \
&& apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Copia o resto do projeto (da pasta backend para o contêiner)
# O ponto (.) no final indica "copiar o conteúdo do diretório atual"
COPY . /app/ 

RUN chmod +x /app/entrypoint.sh
EXPOSE 8000
CMD ["sh", "/app/entrypoint.sh"]