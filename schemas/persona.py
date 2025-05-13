from utils.ma import ma
from marshmallow import fields

from models.persona import Persona
from schemas.usuario import Usuario_Schema
from schemas.distrito import Distrito_Schema

class Persona_Schema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'id_pers',
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

persona_schema = Persona_Schema()
personas_schema = Persona_Schema(many=True)