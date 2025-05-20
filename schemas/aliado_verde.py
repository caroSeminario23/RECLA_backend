from utils.ma import ma
from marshmallow import fields

from models.Aliado_verde import Aliado_verde
from schemas.usuario import Usuario_Schema

class Aliado_verde_Schema(ma.Schema):
    class Meta:
        model = Institucion
        fields = (
            'id_aliado',
            'id_user',
            'nombre',
            'ruc',
            'usuario'
        )

    usuario = ma.Nested(Usuario_Schema)

aliado_verde_schema = Aliado_verde_Schema()
aliados_verdes_schema = Aliado_verde_Schema(many=True)