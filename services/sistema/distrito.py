from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.distrito import Distrito
from schemas.distrito import distrito_schema, distritos_schema

distrito_routes = Blueprint('distrito_routes', __name__)

# Mostrar todos los distritos
@distrito_routes.route('/getDistritos', methods=['GET'])
def get_distritos():
    mensaje = Distrito.query.all()

    if not mensaje:
        data = {
            'status': 404,
            'message': 'No hay distritos registrados'
        }
        return make_response(jsonify(data), 404)
    else:
        result = distritos_schema.dump(mensaje)
        data = {
            'status': 200,
            'message': 'Distritos encontrados',
            'data': result
        }
        return make_response(jsonify(data), 200)