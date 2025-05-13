from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from model.tabla_puntos import TablaPuntos
from schemas.tabla_puntos import tablaPuntos_schema, tablasPuntos_schema

tablaPuntos_routes = Blueprint('tabla_puntos', __name__)

# Visualizar tabla de puntos de una persona
@tablaPuntos_routes.route('/getTablaPuntos', methods=['POST'])
def get_tablaPuntos():
    id_persona = request.json.get('id_persona')

    if not id_persona:
        data = {
            'status': 400,
            'message': 'El id de la persona es requerido'
        }
        return make_response(jsonify(data), 400)

    tablaPuntos = TablaPuntos.query.filter_by(id_pers=id_persona).first()
    
    if not tablaPuntos:
        data = {
            'status': 404,
            'message': 'No se encontro la tabla de puntos'
        }
        return make_response(jsonify(data), 404)
    else:
        result = tablaPuntos_schema.dump(tablaPuntos)
        data = {
            'status': 200,
            'message': 'Tabla de puntos encontrada',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Aumentar puntos de experiencia de una persona
@tablaPuntos_routes.route('/aumentarPuntos', methods=['PUT'])
def aumentar_puntos():
    id_persona = request.json.get('id_persona')
    puntos_exp = request.json.get('puntos_exp')

    if not id_persona or not puntos_exp:
        data = {
            'status': 400,
            'message': 'El id de la persona y los puntos de experiencia son requeridos'
        }
        return make_response(jsonify(data), 400)

    tablaPuntos = TablaPuntos.query.filter_by(id_pers=id_persona).first()
    
    if not tablaPuntos:
        data = {
            'status': 404,
            'message': 'No se encontro la tabla de puntos'
        }
        return make_response(jsonify(data), 404)
    else:
        tablaPuntos.puntos += puntos
        db.session.commit()
        result = tablaPuntos_schema.dump(tablaPuntos)
        data = {
            'status': 200,
            'message': 'Puntos de experiencia aumentados',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Aumentar los puntos de app de una persona
@tablaPuntos_routes.route('/aumentarPuntosApp', methods=['PUT'])
def aumentar_puntos_app():
    id_persona = request.json.get('id_persona')
    puntos_app = request.json.get('puntos_app')

    if not id_persona or not puntos_app:
        data = {
            'status': 400,
            'message': 'El id de la persona y los puntos de app son requeridos'
        }
        return make_response(jsonify(data), 400)

    tablaPuntos = TablaPuntos.query.filter_by(id_pers=id_persona).first()
    
    if not tablaPuntos:
        data = {
            'status': 404,
            'message': 'No se encontro la tabla de puntos'
        }
        return make_response(jsonify(data), 404)
    else:
        tablaPuntos.puntos_app += puntos_app
        db.session.commit()
        result = tablaPuntos_schema.dump(tablaPuntos)
        data = {
            'status': 200,
            'message': 'Puntos de app aumentados',
            'data': result
        }
        return make_response(jsonify(data), 200)