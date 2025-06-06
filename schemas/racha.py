from utils.ma import ma
from marshmallow import fields

from models.racha import Racha
from schemas.eco_aprendiz import Ecoaprendiz_Schema

class Racha_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Racha
        include_fk = True
        include_relationships = True
        fields = (
            'id_racha',
            'id_aprendiz',
            'n_dias'
            #'ecoaprendiz'
        )

    #ecoaprendiz = ma.Nested(Ecoaprendiz_Schema)

racha_schema = Racha_Schema()
rachas_schema = Racha_Schema(many=True)