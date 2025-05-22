import streamlit as st
import requests


url = 'http://127.0.0.1:5000/login'

form = st.form("for_de_login")
form.title("Login")
email_usuario = form.text_input("E-mail")
senha_usuario = form.text_input("Senha", type="password")
btn_login = form.form_submit_button("Enviar")
bota_criar_conta = st.button("Novo por aqui? Cadastre-se agora e faça parte!")

if bota_criar_conta:
    st.switch_page("criar_conta.py")

if btn_login:
    dados_usuario = {"email": email_usuario, "senha": senha_usuario}
    resposta = requests.post(url, json=dados_usuario)
    # print("Status Code:", resposta.status_code)
    # print("Resposta:", resposta.json())

    if resposta.status_code == 200:
        dados_resposta = resposta.json()
        st.session_state["user"] = dados_resposta["usuario"]
        st.session_state["token_acesso"] = dados_resposta["tokens"]["token_acesso"]
        st.session_state["token_atualizacao"] = dados_resposta["tokens"]["token_atualizacao"]
        st.session_state["autenticado"] = True
        form.success(resposta.json()["mensagem"])
        from pprint import pprint
        pprint(st.session_state)
        st.rerun()
    elif resposta.status_code == 400:
        form.warning(resposta.json()["Erro"])
    elif resposta.status_code == 401:
        form.warning(resposta.json()["Erro"])


