from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.usuario import Usuario
from models.eco_aprendiz import Eco_aprendiz
from models.aliado_verde import Aliado_verde
from schemas.usuario import usuario_schema, usuarios_schema
from schemas.eco_aprendiz import ecoaprendiz_schema, ecoaprendices_schema
from schemas.aliado_verde import aliado_schema, aliados_schema

from services.functions.encriptacion import encriptar_contrasena

# RUTAS DE REGISTRO
registro_routes = Blueprint('registro_routes', __name__)

# REGISTRAR ECOAPRENDIZ
@registro_routes.route('/registrarEcoaprendiz', methods=['POST'])
def registrarEcoaprendiz():
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    id_distrito = request.json.get('id_distrito')
    nombre_usuario = request.json.get('nombre_usuario')
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')

    if not nombre or not apellido or not fecha_nacimiento or not id_distrito or not nombre_usuario or not email or not contrasena:
        data = {
            'status': 400,
            'message': 'Todos los campos son requeridos'
        }
        return make_response(jsonify(data), 400)

    # Verificar si el usuario ya existe
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        data = {
            'status': 409,
            'message': 'Este correo ya está registrado con otro usuario'
        }
        return make_response(jsonify(data), 409)
    else:
        # Encriptar la contraseña
        contrasena_encriptada = encriptar_contrasena(contrasena)

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(
            email=email,
            contra=contrasena_encriptada,
        )
        db.session.add(nuevo_usuario) # Agregar el usuario a la sesión
        db.session.commit() # Confirmar los cambios en la base de datos
        result_usuario = usuario_schema.dump(nuevo_usuario) # Serializar el usuario

        # Obtener el ID del nuevo usuario
        id_nuevo_usuario = Usuario.query.filter_by(email=email).first().id_user
        if not id_nuevo_usuario:
            data = {
                'status': 500,
                'message': 'Usuario no encontrado después de la creación'
            }
            return make_response(jsonify(data), 500)

        # Crear un nuevo ecoaprendiz
        nuevo_ecoaprendiz = Eco_aprendiz(
            id_user= id_nuevo_usuario,
            nom_priv=nombre,
            apellido=apellido,
            fec_nac=fecha_nacimiento,
            nom_pub=nombre_usuario,
            id_dist=id_distrito
        )

        db.session.add(nuevo_ecoaprendiz)
        db.session.commit()
        result_ecoaprendiz = ecoaprendiz_schema.dump(nuevo_ecoaprendiz)
        data = {
            'status': 201,
            'message': 'Ecoaprendiz registrado exitosamente',
            'data': result_ecoaprendiz
        }
        return make_response(jsonify(data), 201)


# REGISTRAR ALIADO VERDE
@registro_routes.route('/registrarAliadoVerde', methods=['POST'])
def registrarAliadoVerde():
    nombre = request.json.get('nombre')
    ruc = request.json.get('ruc')
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')

    if not nombre or not ruc or not email or not contrasena:
        data = {
            'status': 400,
            'message': 'Todos los campos son requeridos'
        }
        return make_response(jsonify(data), 400)

    # Verificar si el usuario ya existe
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        data = {
            'status': 409,
            'message': 'Este correo ya está registrado con otro usuario'
        }
        return make_response(jsonify(data), 409)
    else:
        # Encriptar la contraseña
        contrasena_encriptada = encriptar_contrasena(contrasena)

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(
            email=email,
            contra=contrasena_encriptada,
        )
        db.session.add(nuevo_usuario) # Agregar el usuario a la sesión
        db.session.commit() # Confirmar los cambios en la base de datos

        result_usuario = usuario_schema.dump(nuevo_usuario) # Serializar el usuario

        # Obtener el ID del nuevo usuario
        id_nuevo_usuario = Usuario.query.filter_by(email=email).first().id_user
        if not id_nuevo_usuario:
            data = {
                'status': 500,
                'message': 'Usuario no encontrado después de la creación'
            }
            return make_response(jsonify(data), 500)

        # Crear un nuevo aliado verde
        nuevo_aliado_verde = Aliado_verde(
            id_user= id_nuevo_usuario,
            nombre=nombre,
            ruc=ruc
        )

        db.session.add(nuevo_aliado_verde)
        db.session.commit()
        result_aliado_verde = aliado_schema.dump(nuevo_aliado_verde)
        data = {
            'status': 201,
            'message': 'Aliado verde registrado exitosamente',
            'data': result_aliado_verde
        }
        return make_response(jsonify(data), 201)