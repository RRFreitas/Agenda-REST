from common.database import db
from flask_restful import fields

contato_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'telefone': fields.String,
    'operadora_id': fields.Integer
}

class Contato(db.Model):
    __tablename__ = 'contato'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(30))
    telefone = db.Column('telefone', db.String(15))

    operadora_id = db.Column('operadora_id', db.ForeignKey("operadora.id"))

    operadora = db.relationship("Operadora")

    def __init__(self, nome, telefone, operadora_id):
        self.nome = nome
        self.telefone = telefone
        self.operadora_id = operadora_id

    def __str__(self):
        return "<Contato [id = %s, nome = %s, telefone = %s, operadora_id = %s]>" % (self.id, self.nome, self.telefone, self.operadora_id)

    def __repr__(self):
        return self.__str__()