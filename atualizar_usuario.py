import streamlit as st
import requests
import time

url = 'http://127.0.0.1:5000/atualizar'

if not st.session_state["autenticado"]:
    st.warning("Você precisa estar logado para acessar está página")
    st.switch_page("login.py")
    st.rerun()

form = st.form("form_atualizar_usuario")
form.title("Atualize Suas Credenciais Aqui:")
nome_usuario = form.text_input("Atualize Seu Nome")
senha_usuario = form.text_input("Atualize sua Senha", type="password")
btn_atualizar_dados = form.form_submit_button("Atualizar")

if btn_atualizar_dados:
    headers = {
        "Authorization": f'Bearer {st.session_state["token_acesso"]}'
    }

    dados_usuario = {
        "nome": nome_usuario,
        "senha": senha_usuario
    }
    resposta = requests.put(url, json=dados_usuario, headers=headers)

    print("Status Code:", resposta.status_code)
    print("Resposta:", resposta.json())

    if resposta.status_code == 200:
        form.success(resposta.json()["Sucesso"])
        st.session_state['user']['nome'] = resposta.json()["Usuario"]["nome"]
        time.sleep(2)
        st.rerun()
    elif resposta.status_code == 400:
        form.warning(resposta.json()["Erro"])
    elif resposta.status_code == 409:
        form.warning(resposta.json()["Erro"])
