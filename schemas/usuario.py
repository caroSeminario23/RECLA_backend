from utils.ma import ma
from marshmallow import fields

from models.tabla_puntos import TablaPuntos

class Usuario_Schema(ma.Schema):
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