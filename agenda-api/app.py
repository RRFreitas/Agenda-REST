from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from common.database import db
from resources.OperadoraResource import OperadoraResource
from resources.ContatoResource import ContatoResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ifpbinfo@localhost/agenda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

db.init_app(app)

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api')

api.add_resource(OperadoraResource, '/operadoras')
api.add_resource(ContatoResource, '/contatos', '/contatos/<int:contato_id>')

app.register_blueprint(api_bp)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0')