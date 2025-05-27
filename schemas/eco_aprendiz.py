from utils.ma import ma
from marshmallow import fields

from models.eco_aprendiz import Eco_aprendiz
from schemas.usuario import Usuario_Schema
from schemas.distrito import Distrito_Schema

class Ecoaprendiz_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Eco_aprendiz
        include_fk = True
        include_relationships = True
        fields = (
            'id_aprendiz',
            'id_user',
            'nom_priv',
            'apellido',
            'fec_nac',
            'nom_pub',
            'id_dist',
            'usuario',
            'distrito'
        )

    usuario = ma.Nested(Usuario_Schema)
    distrito = ma.Nested(Distrito_Schema)

ecoaprendiz_schema = Ecoaprendiz_Schema()
ecoaprendices_schema = Ecoaprendiz_Schema(many=True)