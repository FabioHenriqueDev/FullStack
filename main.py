import streamlit as st

if "autenticado" in st.session_state:
    pg = st.navigation(
            {
            "HomePage": [
                         st.Page("homepage.py", title="Home"), 
                         st.Page("logout.py", title="Logout"), 
                         st.Page("usuarios_plataforma.py", title="Usuarios"), 
                         st.Page("atualizar_usuario.py", title="Atualizar Credenciais")
                        ]
            }
        )

    pg.run()
else:
    pg = st.navigation(
            {
            "Login ou Crie uma conta": [st.Page("login.py", title="Login"), st.Page("criar_conta.py", title="Criar Conta")],
            }
        )

    pg.run()


    