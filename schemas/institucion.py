from utils.ma import ma
from marshmallow import fields

from models.institucion import Institucion
from schemas.usuario import Usuario_Schema

class Institucion_Schema(ma.Schema):
    class Meta:
        model = Institucion
        fields = (
            'id_inst',
            'id_user',
            'nombre',
            'ruc',
            'usuario'
        )

    usuario = ma.Nested(Usuario_Schema)

institucion_schema = Institucion_Schema()
instituciones_schema = Institucion_Schema(many=True)