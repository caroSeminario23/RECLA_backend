from utils.db import db

class TablaPuntos(db.Model):
    __tablename__ = 'tabla_puntos'

    # Variables
    id_tp = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    id_pers = db.Column(
        db.Integer,
        db.ForeignKey('persona.id_pers'),
        nullable=False
    )

    ptos_exp = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    ptos_app = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    # Relaciones
    persona = db.relationship(
        'Persona',
        backref='tablaPuntosPersona'
    )

    # Constructor
    def __init__(self,
                id_pers,
                ptos_exp,
                ptos_app)