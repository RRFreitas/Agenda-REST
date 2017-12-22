# -*- coding: utf-8 -*-

from flask_restful import Resource, marshal_with, reqparse, request, abort
from models.Contato import Contato, contato_fields
from common.database import db

class ContatoResource(Resource):
    # GET /contatos
    # GET /contatos/<contato_id>
    @marshal_with(contato_fields)
    def get(self, contato_id=None):
        if contato_id is None:
            return Contato.query.all()
        else:
            return Contato.query.filter_by(id=contato_id)

    #POST /contatos
    def post(self):
        try:
            json_data = request.get_json(force=True)

            contato = Contato(json_data['nome'], json_data['telefone'], json_data['operadora_id'])
            db.session.add(contato)
            db.session.commit()

            return 200
        except Exception as err:
            return err

    # DELETE /contatos/<contato_id>
    def delete(self, contato_id):
        try:
            contato = Contato.query.filter_by(id=contato_id).first()

            if contato is None:
                return 404

            db.session.delete(contato)
            db.session.commit()
            return 200
        except Exception as err:
            raise