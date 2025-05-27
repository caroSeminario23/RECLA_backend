from utils.db import db

class Tabla_puntos(db.Model):
    __tablename__ = 'tabla_puntos'

    # Variables
    id_tp = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    id_aprendiz = db.Column(
        db.Integer,
        db.ForeignKey('eco_aprendiz.id_aprendiz'),
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

    # Constructor
    def __init__(self, 
                 id_aprendiz):
        self.id_aprendiz = id_aprendiz