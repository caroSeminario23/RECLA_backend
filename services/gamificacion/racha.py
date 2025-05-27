from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.racha import Racha
from schemas.racha import racha_schema, rachas_schema

racha_routes = Blueprint('racha_routes', __name__)

# Crear una racha para un aprendiz
@racha_routes.route('/crearRacha', methods=['POST'])
def crear_racha():
    id_aprendiz = request.json.get('id_aprendiz')

    if not id_aprendiz:
        data = {
            'status': 400,
            'message': 'El id del aprendiz es requerido'
        }
        return make_response(jsonify(data), 400)

    racha_existente = Racha.query.filter_by(id_aprendiz=id_aprendiz).first()
    
    if racha_existente:
        data = {
            'status': 400,
            'message': 'Ya existe una racha para este aprendiz'
        }
        return make_response(jsonify(data), 400)
    else:
        nueva_racha = Racha(id_aprendiz=id_aprendiz)
        db.session.add(nueva_racha)
        db.session.commit()

        result_racha = racha_schema.dump(nueva_racha)

        # Respuesta personalidad
        if not result_racha:
            data = {
                'status': 500,
                'message': 'Error al crear la racha'
            }
            return make_response(jsonify(data), 500)

        data = {
            'status': 201,
            'message': 'Racha creada exitosamente',
            'data': result_racha
        }
        return make_response(jsonify(data), 201)


# Visualizar racha de un ecoaprendiz
@racha_routes.route('/getRacha', methods=['POST'])
def get_racha():
    id_aprendiz = request.json.get('id_aprendiz')

    if not id_aprendiz:
        data = {
            'status': 400,
            'message': 'El id del aprendiz es requerido'
        }
        return make_response(jsonify(data), 400)

    racha = Racha.query.filter_by(id_aprendiz=id_aprendiz).first()
    
    if not racha:
        data = {
            'status': 404,
            'message': 'No se encontró la racha'
        }
        return make_response(jsonify(data), 404)
    else:
        result_racha = racha_schema.dump(racha)
        data = {
            'status': 200,
            'message': 'Racha encontrada',
            'data': result_racha
        }
        return make_response(jsonify(data), 200)

    
# Aumentar racha de una persona
@racha_routes.route('/incrementarRacha', methods=['PUT'])
def incrementar_racha():
    id_aprendiz = request.json.get('id_aprendiz')

    if not id_aprendiz:
        data = {
            'status': 400,
            'message': 'El id del ecoaprendiz es requerido'
        }
        return make_response(jsonify(data), 400)

    racha = Racha.query.filter_by(id_aprendiz=id_aprendiz).first()
    
    if not racha:
        data = {
            'status': 404,
            'message': 'No se encontro la racha'
        }
        return make_response(jsonify(data), 404)
    else:
        racha.n_dias += 1
        db.session.commit()
        result_racha = racha_schema.dump(racha)
        data = {
            'status': 200,
            'message': 'Racha aumentada en un día',
            'data': result_racha
        }
        return make_response(jsonify(data), 200)


# Reiniciar racha de una persona
@racha_routes.route('/reiniciarRacha', methods=['PUT'])
def reiniciar_racha():
    id_aprendiz = request.json.get('id_aprendiz')

    if not id_aprendiz:
        data = {
            'status': 400,
            'message': 'El id del ecoaprendiz es requerido'
        }
        return make_response(jsonify(data), 400)

    racha = Racha.query.filter_by(id_aprendiz=id_aprendiz).first()
    
    if not racha:
        data = {
            'status': 404,
            'message': 'No se encontro la racha'
        }
        return make_response(jsonify(data), 404)
    else:
        racha.n_dias = 0
        db.session.commit()
        result_racha = racha_schema.dump(racha)
        data = {
            'status': 200,
            'message': 'Racha reiniciada',
            'data': result_racha
        }
        return make_response(jsonify(data), 200)
