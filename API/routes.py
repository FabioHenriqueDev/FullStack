from construtor import app
from services import criar_usuario, login, mostrar_usuarios, atualizar_usuario
from flask_jwt_extended import jwt_required

@app.route("/usuarios", methods=["POST"])
def rota_criar_usuario():
    return criar_usuario()

@app.route("/login", methods=["POST"])
def rota_login():
    return login()

@app.route("/todosusuarios", methods=["GET"])
def rota_mostrar_usuarios():
    return mostrar_usuarios()


@app.route("/atualizar", methods=["PUT"])
@jwt_required()
def rota_atualizar_dados():
    return atualizar_usuario()