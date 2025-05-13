from utils.ma import ma
from marshmallow import fields

from models.distrito import Distrito

class Distrito_Schema(ma.Schema):
    class Meta:
        model = Distrito
        fields = (
            'id_dist',
            'nombre'
        )

invitado_schema = DistritoSchema()
distritos_schema = DistritoSchema(many=True)