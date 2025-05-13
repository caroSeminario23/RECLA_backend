from utils.ma import ma
from marshmallow import fields

from models.racha import Racha
from schemas.persona import Persona_Schema

class Racha_Schema(ma.Schema):
    class Meta:
        model = Racha
        fields = (
            'id_racha',
            'id_pers',
            'n_dias',
            'persona'
        )

    persona = ma.Nested(Persona_Schema)

racha_schema = Racha_Schema()
rachas_schema = Racha_Schema(many=True)