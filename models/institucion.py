from utils.db import db

class Institucion(db.Model):
    __tablename__ = 'institucion'

    # Variables
    id_inst = db.Column(
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

    # Constructor
    def __init__(self,
                id_user,
                nombre,
                ruc):
        self.id_user=id_user
        self.nombre=nombre
        self.ruc=ruc