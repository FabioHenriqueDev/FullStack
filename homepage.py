import streamlit as st

if not st.session_state["autenticado"]:
    st.warning("Você precisa estar logado para acessar está página")
    st.switch_page("login.py")
    st.rerun()
st.title("HomePage")
st.write(f"### Olá {st.session_state['user']['nome']}, seja bem vindo ao nosso sistema!")
