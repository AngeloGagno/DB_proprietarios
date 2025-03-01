## 📌 Sobre o Projeto

O **DB_Proprietarios** é um projeto desenvolvido para consumir o endpoint **Owners** da API da [Avantio](https://www.avantio.com/), uma empresa especializada em **Property Management Software (PMS)**. O objetivo principal é extrair dados dos proprietários de uma conta no software e armazená-los em um banco de dados **PostgreSQL**.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python
- **Banco de Dados**: PostgreSQL
- **Ferramentas**: Requests, SQLAlchemy, dotenv, Docker

## 📄 Documentação

A documentação detalhada do projeto pode ser acessada através do link abaixo:

[📖 Acessar Documentação](https://angelogagno.github.io/DB_proprietarios/)

---

## 📌 Como Executar o Projeto

### 📦 Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.8+
- PostgreSQL
- Pip e virtualenv

### 🔧 Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/angelogagno/DB_proprietarios.git
   cd DB_proprietarios
   ```

2. Crie o arquivo para as variaveis de ambiente:
    ```bash 
    touch .env
    ```

3. Insira as variaveis de ambiente no arquivo .env
    ```bash
    API_AVANTIO='SUA_API'
    Database_url='URL_DO_BANCO'
    ```    

4. Execute o Container:
    ```bash
    docker-compose up --build

## 📬 Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- 📧 Email: angelogagno@gmail.com
- 🔗 LinkedIn: [Angelo Gagno](https://www.linkedin.com/in/angelogagno)
- 🐙 GitHub: [Angelo Gagno](https://github.com/angelogagno)

---

Desenvolvido por [Angelo Gagno](https://github.com/angelogagno).

