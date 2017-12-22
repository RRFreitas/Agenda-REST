# -*- coding: utf-8 -*-

from flask_restful import Resource, marshal_with
from models.Operadora import Operadora, operadora_fields

class OperadoraResource(Resource):
    # GET /operadoras
    @marshal_with(operadora_fields)
    def get(self):
        operadoras = Operadora.query.all()
        return operadoras