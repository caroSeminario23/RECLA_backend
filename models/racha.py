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

    id_aprendiz = db.Column(
        db.Integer,
        db.ForeignKey('eco_aprendiz.id_aprendiz'),
        nullable=False
    )

    n_dias = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    # Relaciones
    ecoaprendiz = db.relationship(
        'Eco_aprendiz',
        backref='Ecoaprendiz_racha'
    )

    # Constructor
    def __init__(self,
                id_aprendiz): 
        self.id_aprendiz=id_aprendiz