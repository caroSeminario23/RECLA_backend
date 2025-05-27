from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from model.usuario import Usuario
from schemas.usuario import usuario_schema, usuarios_schema

# =================================================
# ENCRIPTAR Y DESENCRIPTAR CONTRASEÑA
import bcrypt

# Encriptar contraseña usando bcrypt
def encriptar_contrasena(contrasena):
    # Generar un salt (un valor aleatorio) para la encriptación segura
    salt = bcrypt.gensalt()
    # Encriptar la contraseña
    contrasena_encriptada = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    return contrasena_encriptada.decode('utf-8')

# Desencriptar contraseña usando bcrypt: retorna True o False
def verificar_contrasena(contrasena, contrasena_encriptada):
    # Verificar la contraseña
    return bcrypt.checkpw(contrasena.encode('utf-8'), contrasena_encriptada.encode('utf-8'))

# =================================================
# RUTAS DE USUARIO
usuario_routes = Blueprint('usuario', __name__)

# Iniciar sesión
@usuario_routes.route('/login', methods=['POST'])
def iniciar_sesion():
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')

    if not email or not contrasena:
        data = {
            'status': 400,
            'message': 'El email y la contraseña son requeridos'
        }
        return make_response(jsonify(data), 400)

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
        data = {
            'status': 404,
            'message': 'No se encontro el usuario'
        }
        return make_response(jsonify(data), 404)

    if not verificar_contrasena(contrasena, usuario.contra):
        data = {
            'status': 401,
            'message': 'Contraseña incorrecta'
        }
        return make_response(jsonify(data), 401)
    else:
        result = usuario_schema.dump(usuario)
        data = {
            'status': 200,
            'message': 'Usuario encontrado',
            'data': result
        }
        return make_response(jsonify(data), 200)

# Crear usuario
@usuario_routes.route('/crearUsuario', methods=['POST'])
def crear_usuario():
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')

    if not email or not contrasena:
        data = {
            'status': 400,
            'message': 'El email y la contraseña son requeridos'
        }
        return make_response(jsonify(data), 400)

    usuario = Usuario.query.filter_by(email=email).first()
    
    if usuario:
        data = {
            'status': 409,
            'message': 'Ya existe un usuario con el mismo email'
        }
        return make_response(jsonify(data), 409)
    else:
        # Encriptar la contraseña antes de guardarla
        contrasena_encriptada = encriptar_contrasena(contrasena)
        nuevo_usuario = Usuario(email=email, contra=contrasena_encriptada)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        result = usuario_schema.dump(nuevo_usuario)
        data = {
            'status': 201,
            'message': 'Registro de usuario creado',
            'data': result
        }
        return make_response(jsonify(data), 201)