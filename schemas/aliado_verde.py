from utils.ma import ma
from marshmallow import fields

from models.aliado_verde import Aliado_verde
from schemas.usuario import Usuario_Schema

class Aliado_Schema(ma.Schema):
    class Meta:
        model = Aliado_verde
        fields = (
            'id_aliado',
            'id_user',
            'nombre',
            'ruc',
            'usuario'
        )

    usuario = ma.Nested(Usuario_Schema)

aliado_schema = Aliado_Schema()
aliados_schema = Aliado_Schema(many=True)