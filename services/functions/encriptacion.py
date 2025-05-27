import bcrypt

# Encriptar contraseña usando bcrypt
def encriptar_contrasena(contrasena):
    # Generar un salt (un valor aleatorio) para la encriptación segura
    salt = bcrypt.gensalt()
    # Encriptar la contraseña
    contrasena_encriptada = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    return contrasena_encriptada.decode('utf-8')

# Verificar contraseña usando bcrypt: retorna True o False
def verificar_contrasena(contrasena, contrasena_encriptada):
    return bcrypt.checkpw(contrasena.encode('utf-8'), contrasena_encriptada.encode('utf-8'))