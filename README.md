# 💻 Aplicação Full Stack com Streamlit, Flask e MySQL

Este projeto é uma aplicação full stack desenvolvida como estudo prático de integração entre frontend, backend e banco de dados.

## ✨ Tecnologias Utilizadas

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend (API):** [Flask](https://flask.palletsprojects.com/)  
- **Banco de Dados:** MySQL (em container Docker)  
- **Autenticação:** JWT (JSON Web Tokens)  
- **ORM:** SQLAlchemy  

---

## 📦 Funcionalidades

### 🔐 Autenticação
- **Login de Usuário:** Geração de token de acesso e refresh usando JWT.
- **Criação de Usuário:** Cadastro com verificação de e-mail e nome únicos.
- **Atualização de Usuário:** Permite alteração do nome e senha.

---

## 🧠 Estrutura do Projeto

### 🔸 Backend (Flask API)

A API possui os seguintes endpoints principais:

| Método | Rota         | Descrição                            |
|--------|--------------|----------------------------------------|
| POST   | `/login`     | Realiza o login e retorna os tokens    |
| POST   | `/cadastro`  | Cria um novo usuário                   |
| PUT    | `/atualizar` | Atualiza o nome e senha do usuário     |

A autenticação é feita com JWT, e o token é exigido nos endpoints protegidos.

---

### 🔹 Frontend (Streamlit)

O frontend desenvolvido com Streamlit realiza as seguintes funções:

- Interface de login e cadastro.
- Tela protegida para atualizar os dados do usuário.
- Uso de `st.session_state` para armazenar tokens de autenticação e dados do usuário logado.
- Requisições autenticadas para o backend com uso de headers `Authorization: Bearer <token>`.

---

### 🔸 Banco de Dados (MySQL no Docker)

- O banco de dados utilizado é o MySQL.
- Ele é executado dentro de um container Docker para facilitar o ambiente de desenvolvimento.
- A conexão é feita a partir da API Flask utilizando SQLAlchemy.

---

## 🐳 Como subir o MySQL com Docker

```bash
docker run --name mysql-streamlit -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=seu_banco -p 3306:3306 -d mysql:8.0
