from utils.db import db

class Aliado_verde(db.Model):
    __tablename__ = 'aliado_verde'

    # Variables
    id_aliado = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    id_user = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id_user'),
        nullable=False
    )

    nombre = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    ruc = db.Column(
        db.String(11),
        nullable=False,
        unique=True
    )

    # Relaciones
    usuario = db.relationship(
        'Usuario',
        backref='institucionUsuario'
    )

    # Constructor
    def __init__(self,
                id_user,
                nombre,
                ruc):
        self.id_user=id_user
        self.nombre=nombre
        self.ruc=ruc