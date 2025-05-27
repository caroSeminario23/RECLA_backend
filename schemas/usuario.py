from utils.ma import ma
from marshmallow import fields

from models.usuario import Usuario

class Usuario_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        fields = (
            'id_user',
            'email',
            'contra',
            'fec_reg'
        )

usuario_schema = Usuario_Schema()
usuarios_schema = Usuario_Schema(many=True)