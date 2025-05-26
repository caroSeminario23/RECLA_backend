from utils.db import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    # Variables
    id_user = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    email = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    contra = db.Column(
        db.String(255),
        nullable=False
    )

    fec_reg = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now()
    )

    # Constructor
    def __init__(self,
                email,
                contra):
        self.email=email
        self.contra=contra