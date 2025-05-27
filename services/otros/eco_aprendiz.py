from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from model.eco_aprendiz import Eco_aprendiz
from schemas.eco_aprendiz import eco_aprendiz_schema, eco_aprendices_schema

eco_aprendiz_routes = Blueprint('eco_aprendiz_routes', __name__)

# Buscar ecoaprendiz por ID
@eco_aprendiz_routes.route('/getEcoAprendiz', methods=['POST'])
def get_eco_aprendiz():
    id_aprendiz = request.json.get('id_aprendiz')

    if not id_aprendiz:
        data = {
            'status': 400,
            'message': 'El id del eco aprendiz es requerido'
        }
        return make_response(jsonify(data), 400)

    ecoaprendiz = Eco_aprendiz.query.filter_by(id_aprendiz=id_aprendiz).first()
    
    if not ecoaprendiz:
        data = {
            'status': 404,
            'message': 'No se encontro al eco aprendiz'
        }
        return make_response(jsonify(data), 404)
    else:
        result = eco_aprendiz_schema.dump(persona)
        data = {
            'status': 200,
            'message': 'Eco aprendiz encontrado',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Verificar si existe un ecoaprendiz con el mismo nombre público
@eco_aprendiz_routes.route('/verificarEcoAprendiz', methods=['POST'])
def verificar_eco_aprendiz():
    nombre = request.json.get('nombre_publico')

    if not nombre:
        data = {
            'status': 400,
            'message': 'El nombre público es requerido'
        }
        return make_response(jsonify(data), 400)

    ecoaprendiz = Eco_aprendiz.query.filter_by(nom_pub=nombre).first()
    
    if ecoaprendiz:
        data = {
            'status': 409,
            'message': 'Ya existe un ecoaprendiz con el mismo nombre público'
        }
        return make_response(jsonify(data), 409)
    else:
        data = {
            'status': 200,
            'message': 'Nombre público disponible'
        }
        return make_response(jsonify(data), 200)

# Crear ecoaprendiz
@persona_routes.route('/crearEcoAprendiz', methods=['POST'])
def crear_eco_aprendiz():
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
    id_aprendiz = request.json.get('id_aprendiz')
    id_distrito = request.json.get('id_distrito')

    if not id_aprendiz or not id_distrito:
        data = {
            'status': 400,
            'message': 'El id de la persona y el id del distrito son requeridos'
        }
        return make_response(jsonify(data), 400)

    persona = Persona.query.filter_by(id_pers=id_aprendiz).first()
    
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