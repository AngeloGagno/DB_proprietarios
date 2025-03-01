# Usando uma imagem oficial do Python
FROM python:3.11

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos necessários para a instalação do Poetry e dependências
COPY pyproject.toml poetry.lock ./

# Instalando o Poetry
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copiando o restante do código
COPY . .

# Comando para rodar a aplicação
CMD ["poetry", "run", "python", "src/main.py"]
