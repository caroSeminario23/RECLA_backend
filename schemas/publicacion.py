from utils.ma import ma
from marshmallow import fields

from models.publicacion import Publicacion

class Publicacion_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion
        include_fk = True
        include_relationships = True
        fields = (
            'id_pub',
            'id_vend',
            'fec_reg',
            'foto_link',
            'descrip',
            'tipo',
            'estado',
            'precio'
        )

publicacion_schema = Publicacion_Schema()
publicaciones_schema = Publicacion_Schema(many=True)