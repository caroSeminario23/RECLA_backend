from utils.db import db

class Material(db.Model):
    __tablename__ = 'material'

    # Variables
    id_mat = db.Column(
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
        self.nombre = nombre