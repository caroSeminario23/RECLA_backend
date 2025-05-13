from utils.ma import ma
from marshmallow import fields

from models.tabla_puntos import TablaPuntos
from schemas.persona import Persona_Schema

class TablaPuntos_Schema(ma.Schema):
    class Meta:
        model = TablaPuntos
        fields = (
            'id_tp',
            'id_pers',
            'ptos_exp',
            'ptos_app',
            'persona'
        )

    persona = ma.Nested(Persona_Schema)

tablaPuntos_schema = TablaPuntos_Schema()
tablasPuntos_schema = TablaPuntos_Schema(many=True)