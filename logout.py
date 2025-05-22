import streamlit as st

if not st.session_state["autenticado"]:
    st.warning("Você precisa estar logado para acessar está página")
    st.switch_page("login.py")
    st.rerun()

st.title("Deslogar da sua conta:")
btn_deslogar = st.button("Logout")

if btn_deslogar:
    st.session_state.clear()
    st.rerun()