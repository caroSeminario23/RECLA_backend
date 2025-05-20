from utils.ma import ma
from marshmallow import fields

from models.persona import Persona
from schemas.usuario import Usuario_Schema
from schemas.distrito import Distrito_Schema

class Eco_aprendiz_Schema(ma.Schema):
    class Meta:
        model = Eco_aprendiz
        fields = (
            'id_aprendiz',
            'id_user',
            'nom_priv',
            'apellido',
            'anio_nac',
            'nom_pub',
            'id_dist',
            'usuario',
            'distrito'
        )

    usuario = ma.Nested(Usuario_Schema)
    distrito = ma.Nested(Distrito_Schema)

eco_aprendiz_schema = Eco_aprendiz_Schema()
eco_aprendices_schema = Eco_aprendiz_Schema(many=True)