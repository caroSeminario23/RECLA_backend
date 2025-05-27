from utils.db import db

class Publicacion(db.Model):
    __tablename__ = 'publicacion'

    # Variables
    id_pub = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    id_vend = db.Column(
        db.Integer,
        db.ForeignKey('eco_aprendiz.id_aprendiz'),
        nullable=False
    )

    fec_reg = db.Column(
        db.DateTime,
        nullable=False
    )

    foto_link = db.Column(
        db.Text,
        nullable=False
    )

    descrip = db.Column(
        db.String(250),
        nullable=False
    )

    tipo = db.Column(
        db.Boolean,
        nullable=False
    )

    estado = db.Column(
        db.Boolean,
        nullable=False
    )

    precio = db.Column(
        db.Integer,
        nullable=False
    )

    # Relaciones
    eco_aprendiz = db.relationship(
        'Eco_aprendiz',
        backref='ecoaprendiz_publicacion'
    )

    # Constructor
    def __init__(self,
                 id_vend,
                 fec_reg,
                 foto_link,
                 descrip,
                 tipo,
                 estado,
                 precio):
        self.id_vend = id_vend
        self.fec_reg = fec_reg
        self.foto_link = foto_link
        self.descrip = descrip
        self.tipo = tipo
        self.estado = estado
        self.precio = precio