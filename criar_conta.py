import streamlit as st
import requests

url = 'http://127.0.0.1:5000/usuarios'

form = st.form("form_criar_conta")
form.title("Criar Conta")
nome_usuario = form.text_input("Nome do Usuário")
email_usuario = form.text_input("Email do Usuário")
senha_usuario = form.text_input("Senha do Usuário", type="password")
btn_criar_conta = form.form_submit_button("Criar Conta")
botao_login = st.button("Já tem uma conta? Faça o login aqui")

if botao_login:
    st.switch_page("login.py")


if btn_criar_conta:
    dados_usuario = {
        "nome": nome_usuario, 
        "email": email_usuario, 
        "senha": senha_usuario
    }

    resposta = requests.post(url, json=dados_usuario)
    print("Status Code:", resposta.status_code)
    print("Resposta:", resposta.json())

    if resposta.status_code == 200:
        form.success(resposta.json()["Sucesso"])
        st.switch_page("login.py")
    elif resposta.status_code == 400:
        form.warning(resposta.json()["Erro"])
    elif resposta.status_code == 409:
        form.warning(resposta.json()["Erro"])
    elif resposta.status_code == 401:
        form.warning(resposta.json()["Erro"])


