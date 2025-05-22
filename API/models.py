from extensions import db, bcrypt
import re
from flask import jsonify
from erros import (
        
        EmailVazioError, 
        EmailInvalidoError, 
        SenhaVazioError, 
        SenhaInvalidaError, 
        NomeInvalidoError, 
        NomeVazioError
    
    )

class Usuario(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True, autoincrement=True)
    nome = db.Column("nome", db.String(100), nullable=False)
    email = db.Column("email", db.String(200), nullable=False, unique=True)
    senha = db.Column("senha", db.String(200), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = self.validar_nome(nome)
        self.email = self.validar_email(email)
        self.senha = self.validar_senha(senha)

    def validar_email(self, email):
        email = email.strip().lower()
        if len(email) == 0:
            raise EmailVazioError("Preencha o campo do email")
        email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_padrao, email):
            raise EmailInvalidoError("E-mail Inválido")
        return email

    def validar_senha(self, senha):
        if len(senha) < 1:
            raise SenhaVazioError("Preencha o campo da senha")
        if len(senha) < 6:
            raise SenhaInvalidaError("A senha tem que ter no mínimo 6 caracteres")
        hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        return hash_senha
    
    def validar_nome(self, nome):
        if len(nome) < 1:
            raise NomeVazioError("Preencha o campo do nome")
        if len(nome) < 2:
            raise NomeInvalidoError("Digite um nome válido")
        
        return nome
    
    
        
           


