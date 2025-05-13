from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from model.institucion import Institucion
from schemas.institucion import institucion_schema, instituciones_schema

institucion_routes = Blueprint('institucion_routes', __name__)

# Buscar institución por ID
@institucion_routes.route('/getInstitucion', methods=['POST'])
def get_institucion():
    id_institucion = request.json.get('id_institucion')

    if not id_institucion:
        data = {
            'status': 400,
            'message': 'El id de la institucion es requerido'
        }
        return make_response(jsonify(data), 400)

    institucion = Institucion.query.filter_by(id_inst=id_institucion).first()
    
    if not institucion:
        data = {
            'status': 404,
            'message': 'No se encontro la institucion'
        }
        return make_response(jsonify(data), 404)
    else:
        result = institucion_schema.dump(institucion)
        data = {
            'status': 200,
            'message': 'Institucion encontrada',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Verificar si existe una institucion con el mismo nombre y RUC
@institucion_routes.route('/verificarInstitucion', methods=['POST'])
def verificar_institucion():
    nombre = request.json.get('nombre')
    ruc = request.json.get('ruc')

    if not nombre or not ruc:
        data = {
            'status': 400,
            'message': 'El nombre y el RUC de la institucion son requeridos'
        }
        return make_response(jsonify(data), 400)

    institucion = Institucion.query.filter_by(nombre=nombre, ruc=ruc).first()

    if institucion:
        data = {
            'status': 409,
            'message': 'Ya existe una institucion con el mismo nombre y RUC'
        }
        return make_response(jsonify(data), 409)
    else:
        data = {
            'status': 200,
            'message': 'No existe una institucion con el mismo nombre y RUC'
        }
        return make_response(jsonify(data), 200)

# Crear institución
@institucion_routes.route('/crearInstitucion', methods=['POST'])
def crear_institucion():
    id_usuario = request.json.get('id_usuario')
    nombre = request.json.get('nombre')
    ruc = request.json.get('ruc')

    if not id_usuario or not nombre or not ruc:
        data = {
            'status': 400,
            'message': 'El id del usuario, nombre y RUC son requeridos'
        }
        return make_response(jsonify(data), 400)

    institucion = Institucion.query.filter_by(nombre=nombre, ruc=ruc).first()
    
    if institucion:
        data = {
            'status': 409,
            'message': 'Ya existe una institucion con el mismo nombre y RUC'
        }
        return make_response(jsonify(data), 409)
    else:
        nueva_institucion = Institucion(id_user=id_usuario, nombre=nombre, ruc=ruc)
        db.session.add(nueva_institucion)
        db.session.commit()
        
        result = institucion_schema.dump(nueva_institucion)
        data = {
            'status': 201,
            'message': 'Registro de institucion creado',
            'data': result
        }
        return make_response(jsonify(data), 201)