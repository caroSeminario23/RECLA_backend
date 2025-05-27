from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.usuario import Usuario
from models.eco_aprendiz import Eco_aprendiz
from models.aliado_verde import Aliado_verde
from schemas.usuario import usuario_schema, usuarios_schema
from schemas.eco_aprendiz import ecoaprendiz_schema, ecoaprendices_schema
from schemas.aliado_verde import aliado_schema, aliados_schema

from services.functions.encriptacion import verificar_contrasena

# RUTAS DE INICIO DE SESIÓN
inicio_sesion_routes = Blueprint('inicio_sesion', __name__)

# INICIOR SESIÓN DE ECOAPRENDIZ
@inicio_sesion_routes.route('/iniciarSesionEcoaprendiz', methods=['POST'])
def iniciarSesionEcoaprendiz():
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')

    if not email or not contrasena:
        data = {
            'status': 400,
            'message': 'Email y contraseña son requeridos'
        }
        return make_response(jsonify(data), 400)

    # Verificar si el usuario existe
    id_usuario = buscarUsuario(email, contrasena)

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario:
        data = {
            'status': 404,
            'message': 'Usuario no encontrado'
        }
        return make_response(jsonify(data), 404)
    else:
        # Verificar que la contraseña sea igual a la encriptada
        contrasena_encriptada = usuario.contra
        if not verificar_contrasena(contrasena, contrasena_encriptada):
            data = {
                'status': 401,
                'message': 'Contraseña incorrecta'
            }
            return make_response(jsonify(data), 401)
        else:
            # Buscar el ecoaprendiz asociado al usuario
            id_usuario = usuario.id_user
            ecoaprendiz = Eco_aprendiz.query.filter_by(id_user=id_usuario).first()
            if not ecoaprendiz:
                data = {
                    'status': 404,
                    'message': 'Ecoaprendiz no encontrado'
                }
                return make_response(jsonify(data), 404)
            else:
                result_ecoaprendiz = ecoaprendiz_schema.dump(ecoaprendiz)
                data = {
                    'status': 200,
                    'message': 'Inicio de sesión exitoso',
                    'data': result_ecoaprendiz
                }
                return make_response(jsonify(data), 200)

# INICIAR SESIÓN DE ALIADO VERDE
@inicio_sesion_routes.route('/iniciarSesionAliadoVerde', methods=['POST'])
def iniciarSesionAliadoVerde():
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')

    if not email or not contrasena:
        data = {
            'status': 400,
            'message': 'Email y contraseña son requeridos'
        }
        return make_response(jsonify(data), 400)

    # Verificar si el usuario existe
    id_usuario = buscarUsuario(email, contrasena)

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario:
        data = {
            'status': 404,
            'message': 'Usuario no encontrado'
        }
        return make_response(jsonify(data), 404)
    else:
        # Verificar que la contraseña sea igual a la encriptada
        contrasena_encriptada = usuario.contra
        if not verificar_contrasena(contrasena, contrasena_encriptada):
            data = {
                'status': 401,
                'message': 'Contraseña incorrecta'
            }
            return make_response(jsonify(data), 401)
        else:
            # Buscar el aliado verde asociado al usuario
            id_usuario = usuario.id_user
            aliado_verde = Aliado_verde.query.filter_by(id_user=id_usuario).first()
            if not aliado_verde:
                data = {
                    'status': 404,
                    'message': 'Aliado verde no encontrado'
                }
                return make_response(jsonify(data), 404)
            else:
                result_aliado = aliado_schema.dump(aliado_verde)
                data = {
                    'status': 200,
                    'message': 'Inicio de sesión exitoso',
                    'data': result_aliado
                }
                return make_response(jsonify(data), 200)