from flask import Flask, request, jsonify
from flask_jwt_extended import (
    jwt_required, 
    create_access_token, 
    create_refresh_token, 
    get_jwt_identity
)
from extensions import db
from construtor import app
from erros import (
        
        EmailVazioError, 
        EmailInvalidoError, 
        SenhaVazioError, 
        SenhaInvalidaError, 
        NomeInvalidoError, 
        NomeVazioError
    
    )
from models import Usuario
import re
from extensions import bcrypt

# Rota criar Usuario
def criar_usuario():
    dados = request.get_json()

    nome_existente = db.session.query(Usuario).filter_by(nome=dados["nome"]).first()
    if nome_existente:
        return jsonify({"Erro": "Esse nome de Usuário ja existe."}), 409
    email_existente = db.session.query(Usuario).filter_by(email=dados["email"]).first()
    if email_existente:
        return jsonify({"Erro": "Esse email ja existe no banco de dados"}), 409

    try:
        usuario = Usuario(
            nome=dados["nome"], 
            email=dados["email"], 
            senha=dados["senha"]
            )
    except (EmailVazioError, EmailInvalidoError, SenhaVazioError, SenhaInvalidaError, NomeVazioError, NomeInvalidoError) as e:
        return jsonify({"Erro": e.mensagem}), 400

    db.session.add(usuario)
    db.session.commit()

 
    return jsonify(
       {
           "Sucesso": "Usuario Criado com Sucesso",
           "Credenciais": {
               "id": usuario.id,
               "nome": usuario.nome,
               "email": usuario.email
           }
       }

    )

# Rota de Login
def login():
    dados = request.get_json()
    email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if len(dados["email"]) < 1:
        return jsonify({"Erro": "Preenhca o campo de email"}), 400
    if not re.match(email_padrao, dados["email"]):
        return jsonify({"Erro": "Digite um E-mail válido"}), 400
    if len(dados["senha"]) < 1:
        return jsonify({"Erro": "Preenhca o campo de senha"}), 400
    if len(dados["senha"]) < 6:
        return jsonify({"Erro": "A senha deve ter no mínimo 6 caracteres"}), 400
    
    usuario = db.session.query(Usuario).filter_by(email=dados["email"]).first()
    
    if not usuario:
        return jsonify({"Erro": "E-mail ou senha incorretos"}), 401
    
    if not bcrypt.check_password_hash(usuario.senha, dados['senha']):
        return jsonify({'Erro': 'E-mail ou Senha incorretos'}), 401
    
    token_acesso = create_access_token(identity=usuario.email)
    token_atualizacao = create_refresh_token(identity=usuario.email)

    return jsonify(
        {
            "mensagem": "Login feito com sucesso",
            "usuario": {
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email
            },
            "tokens": {
                "token_acesso": token_acesso,
                "token_atualizacao": token_atualizacao
            }
        }
    ), 200


# Rota de Mostrar Usuários
def mostrar_usuarios():
    lista_usuarios = Usuario.query.all()
    usuarios = [{"nome": usuario.nome, "email": usuario.email} for usuario in lista_usuarios]
    return jsonify(usuarios)


# Rota atualizar Usuario
def atualizar_usuario():
    dados = request.get_json()
    email_usuario = get_jwt_identity()
    usuario = db.session.query(Usuario).filter_by(email=email_usuario).first()

    if not usuario:
        return jsonify({"Erro": "Uuario não encontrado"})

    nome_existente = db.session.query(Usuario).filter(Usuario.nome == dados["nome"], Usuario.id != usuario.id).first() # Comparando se tem algum valor da coluna de nome que seje o que o usuario digitou mas a coluna de id tem que ser diferente do id do user
    
    if nome_existente:
        return jsonify({"Erro": "Esse nome ja existe no banco de dados"}), 409
    
    if len(dados["nome"]) < 1:
        return jsonify({"Erro": "Preencha o campo de nome"}), 400
    if len(dados["nome"]) < 1:
        return jsonify({"Erro": "Nome Invalido"}), 400
    
    if len(dados["senha"]) < 1:
        return jsonify({"Erro": "Preenhca o campo de senha"}), 400
    if len(dados["senha"]) < 6:
        return jsonify({"Erro": "A senha deve ter no mínimo 6 caracteres"}), 400
    
    usuario.nome = dados["nome"]
    usuario.senha = bcrypt.generate_password_hash(dados["senha"]).decode('utf-8')

    db.session.commit()

    return jsonify(
        {
            "Sucesso": "Usuario Atualizado com Sucesso",
            "Usuario":{
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email
            }
        }
    ), 200
    

    
    

    
    
