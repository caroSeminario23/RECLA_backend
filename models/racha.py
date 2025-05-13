from utils.db import db

class Racha(db.Model):
    __tablename__ = 'racha'

    # Variables
    id_racha = db.Column(
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

    n_dias = db.Column(
        db.Integer,
        nullable=False
    )

    # Relaciones
    persona = db.relationship(
        'Persona',
        backref='rachaPersona'
    )

    # Constructor
    def __init__(self,
                id_pers,
                n_dias): 
        self.id_pers=id_pers
        self.n_dias=n_dias