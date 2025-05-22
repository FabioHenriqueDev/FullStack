import streamlit as st
import requests

if not st.session_state["autenticado"]:
    st.warning("Você precisa estar logado para acessar está página")
    st.switch_page("login.py")
    st.rerun()

url = 'http://127.0.0.1:5000/todosusuarios'

st.markdown("# 👥 Usuários da Plataforma:")
resposta = requests.get(url).json()

for item in resposta:
    with st.container():
        st.markdown(f"""
        <div style="padding: 15px; border-radius: 10px; background-color: #000; margin-bottom: 10px;">
            <strong>👤 Nome:</strong> {item["nome"]}<br>
            <strong>📧 Email:</strong> {item["email"]}
        </div>
        """, unsafe_allow_html=True)


