import requests
import json

requests.post("http://localhost:5000/api/contatos", data=json.dumps({'contato': {'nome': 'Rennan', 'telefone':'9999999', 'operadora_id': 1}}))