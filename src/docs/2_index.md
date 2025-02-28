# 🍍Comandos e Estrutura do Projeto

## 🚀 Comandos Úteis
Abaixo estão os principais comandos para configurar e executar o projeto:

```
# Clonar o repositório
git clone [repositorio]

# Acessar o diretório do repositório
cd ./[repositorio]

# Criar o arquivo de configuração das variáveis
touch .env

# Executar a extração e envio de dados para o banco de dados
docker compose up --build
```

---

## 📂 Estrutura de Pastas do Projeto
A estrutura do projeto é organizada da seguinte maneira:

```
src/
│── API/
│   ├── classes_model.py  # Classes necessárias para o projeto.
│   ├── data_model.py      # Extração do Raw_data e criação da tabela.
│   ├── raw_data/         # Diretório contendo os dados extraídos da API em JSON.
│
│── Database/
│   ├── database.py       # Configuração da conexão e sessão de acesso ao banco de dados.
│   ├── models.py         # Definição das tabelas do banco de dados.
│
│── docs/
│   ├── index.md          # Documentação do projeto.
│
│── Fetch/
│   ├── commit.py         # Função para envio dos dados para o banco de dados.
```

---

💡 **Dicas:**
- Certifique-se de configurar corretamente o arquivo `.env` antes de rodar o projeto.
- Para visualizar a documentação localmente, utilize `mkdocs serve`.


