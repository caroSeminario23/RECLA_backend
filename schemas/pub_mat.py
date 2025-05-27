from utils.ma import ma
from marshmallow import fields

from models.pub_mat import Pub_mat
from schemas.publicacion import Publicacion_Schema
from schemas.material import Material_Schema

class Pub_mat_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pub_mat
        include_fk = True
        include_relationships = True
        fields = (
            'id_pub',
            'id_mat',
            'publicacion',
            'material'
        )

    publicacion = ma.Nested('Publicacion_Schema')
    material = ma.Nested('Material_Schema')

pub_mat_schema = Pub_mat_Schema()
pub_mats_schema = Pub_mat_Schema(many=True)