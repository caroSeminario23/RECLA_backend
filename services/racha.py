from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from model.racha import Racha
from schemas.racha import racha_schema, rachas_schema

racha_routes = Blueprint('racha_routes', __name__)

# Visualizar racha de una persona
@racha_routes.route('/getRacha', methods=['POST'])
def get_racha():
    id_persona = request.json.get('id_persona')

    if not id_persona:
        data = {
            'status': 400,
            'message': 'El id de la persona es requerido'
        }
        return make_response(jsonify(data), 400)

    racha = Racha.query.filter_by(id_pers=id_persona).first()
    
    if not racha:
        data = {
            'status': 404,
            'message': 'No se encontro la racha'
        }
        return make_response(jsonify(data), 404)
    else:
        result = racha_schema.dump(racha)
        data = {
            'status': 200,
            'message': 'Racha encontrada',
            'data': result
        }
        return make_response(jsonify(data), 200)
    }

# Aumentar racha de una persona
@racha_routes.route('/aumentarRacha', methods=['PUT'])
def aumentar_racha():
    id_persona = request.json.get('id_persona')

    if not id_persona:
        data = {
            'status': 400,
            'message': 'El id de la persona es requerido'
        }
        return make_response(jsonify(data), 400)

    racha = Racha.query.filter_by(id_pers=id_persona).first()
    
    if not racha:
        data = {
            'status': 404,
            'message': 'No se encontro la racha'
        }
        return make_response(jsonify(data), 404)
    else:
        racha.n_dias += 1
        db.session.commit()
        result = racha_schema.dump(racha)
        data = {
            'status': 200,
            'message': 'Racha aumentada en un día',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Reiniciar racha de una persona
@racha_routes.route('/reiniciarRacha', methods=['PUT'])
def reiniciar_racha():
    id_persona = request.json.get('id_persona')

    if not id_persona:
        data = {
            'status': 400,
            'message': 'El id de la persona es requerido'
        }
        return make_response(jsonify(data), 400)

    racha = Racha.query.filter_by(id_pers=id_persona).first()
    
    if not racha:
        data = {
            'status': 404,
            'message': 'No se encontro la racha'
        }
        return make_response(jsonify(data), 404)
    else:
        racha.n_dias = 0
        db.session.commit()
        result = racha_schema.dump(racha)
        data = {
            'status': 200,
            'message': 'Racha reiniciada',
            'data': result
        }
        return make_response(jsonify(data), 200)
