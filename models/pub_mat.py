from utils.db import db

class Pub_mat(db.Model):
    __tablename__ = 'pub_mat'

    # Variables
    id_pub = db.Column(
        db.Integer,
        db.ForeignKey('publicacion.id_pub'),
        nullable=False
    )

    id_mat = db.Column(
        db.Integer,
        db.ForeignKey('material.id_mat'),
        nullable=False
    )

    # Relaciones
    publicacion = db.relationship(
        'Publicacion',
        backref='publicacion_pubmat'
    )

    material = db.relationship(
        'Material',
        backref='material_pubmat'
    )

    # Constructor
    def __init__(self, id_pub, id_mat):
        self.id_pub = id_pub
        self.id_mat = id_mat