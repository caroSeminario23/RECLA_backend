from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from model.persona import Persona
from schemas.persona import persona_schema, personas_schema

persona_routes = Blueprint('persona_routes', __name__)

# Buscar persona por ID
@persona_routes.route('/getPersona', methods=['POST'])
def get_persona():
    id_persona = request.json.get('id_persona')

    if not id_persona:
        data = {
            'status': 400,
            'message': 'El id de la persona es requerido'
        }
        return make_response(jsonify(data), 400)

    persona = Persona.query.filter_by(id_pers=id_persona).first()
    
    if not persona:
        data = {
            'status': 404,
            'message': 'No se encontro la persona'
        }
        return make_response(jsonify(data), 404)
    else:
        result = persona_schema.dump(persona)
        data = {
            'status': 200,
            'message': 'Persona encontrada',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Verificar si existe una persona con el mismo nombre público
@persona_routes.route('/verificarPersona', methods=['POST'])
def verificar_persona():
    nombre = request.json.get('nombre_publico')

    if not nombre:
        data = {
            'status': 400,
            'message': 'El nombre público es requerido'
        }
        return make_response(jsonify(data), 400)

    persona = Persona.query.filter_by(nom_pub=nombre).first()
    
    if persona:
        data = {
            'status': 409,
            'message': 'Ya existe una persona con el mismo nombre público'
        }
        return make_response(jsonify(data), 409)
    else:
        data = {
            'status': 200,
            'message': 'Nombre público disponible'
        }
        return make_response(jsonify(data), 200)

# Crear persona
@persona_routes.route('/crearPersona', methods=['POST'])
def crear_persona():
    id_usuario = request.json.get('id_usuario')
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    nombre_publico = request.json.get('nombre_publico')
    id_distrito = request.json.get('id_distrito')

    if not id_usuario or not nombre or not apellido or not fecha_nacimiento or not nombre_publico or not id_distrito:
        data = {
            'status': 400,
            'message': 'Todos los campos son requeridos'
        }
        return make_response(jsonify(data), 400)
    persona = Persona.query.filter_by(id_usuario=id_usuario).first()
    if persona:
        data = {
            'status': 409,
            'message': 'Ya existe una persona con el mismo id de usuario'
        }
        return make_response(jsonify(data), 409)
    else:
        nueva_persona = Persona(id_user=id_usuario, nom_priv=nombre, apellido=apellido, anio_nac=fecha_nacimiento, nom_pub=nombre_publico, id_dist=id_distrito)
        db.session.add(nueva_persona)
        db.session.commit()
        
        result = persona_schema.dump(nueva_persona)
        data = {
            'status': 201,
            'message': 'Registro de persona creado',
            'data': result
        }
        return make_response(jsonify(data), 201)

# Actualizar ubicación de la persona (distrito)
@persona_routes.route('/actualizarUbicacion', methods=['PUT'])
def actualizar_ubicacion():
    id_persona = request.json.get('id_persona')
    id_distrito = request.json.get('id_distrito')

    if not id_persona or not id_distrito:
        data = {
            'status': 400,
            'message': 'El id de la persona y el id del distrito son requeridos'
        }
        return make_response(jsonify(data), 400)

    persona = Persona.query.filter_by(id_pers=id_persona).first()
    
    if not persona:
        data = {
            'status': 404,
            'message': 'No se encontro la persona'
        }
        return make_response(jsonify(data), 404)
    else:
        persona.id_dist = id_distrito
        db.session.commit()
        result = persona_schema.dump(persona)
        data = {
            'status': 200,
            'message': 'Ubicación actualizada',
            'data': result
        }
        return make_response(jsonify(data), 200)