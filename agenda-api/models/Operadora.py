from common.database import db
from flask_restful import fields

operadora_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'codigo': fields.Integer,
    'categoria': fields.String
}

class Operadora(db.Model):
    __tablename__ = 'operadora'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(15))
    codigo = db.Column('codigo', db.Integer)
    categoria = db.Column('categoria', db.String(5))

    def __init__(self, nome, codigo, categoria):
        self.nome = nome
        self.codigo = codigo
        self.categoria = categoria