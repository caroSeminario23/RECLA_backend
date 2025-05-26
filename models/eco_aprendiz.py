from utils.db import db

class Eco_aprendiz(db.Model):
    __tablename__ = 'eco_aprendiz'

    # Variables
    id_aprendiz = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    id_user = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id_user')
        nullable=False
    )

    nom_priv = db.Column(
        db.String(70),
        nullable=False,
    )

    apellido = db.Column(
        db.String(100),
        nullable=False,
    )

    fec_nac = db.Column(
        db.Date,
        nullable=False
    )

    nom_pub = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    id_dist = db.Column(
        db.Integer,
        db.ForeignKey('distrito.id_dist'),
        nullable=False
    )

    # Relaciones
    usuario = db.relationship(
        'Usuario',
        backref='Usuario_ecoaprendiz'
    )

    distrito = db.relationship(
        'Distrito',
        backref='Ecoaprendiz_distrito'
    )

    # Constructor
    def __init__(self,
                id_user,
                nom_priv,
                apellido,
                fec_nac,
                nom_pub,
                id_dist):
        self.id_user=id_user
        self.nom_priv=nom_priv
        self.apellido=apellido
        self.fec_nac=fec_nac
        self.nom_pub=nom_pub
        self.id_dist=id_dist