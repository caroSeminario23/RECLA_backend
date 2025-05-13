from utils.db import db

class Distrito(db.Model):
    __tablename__ = 'distrito'

    # Variables
    id_dist = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    nombre = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    # Constructor
    def __init__(self, 
                nombre):
        self.nombre=nombre