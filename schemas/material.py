from utils.ma import ma
from marshmallow import fields

from models.material import Material

class Material_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Material
        include_fk = True
        include_relationships = True
        fields = (
            'id_mat',
            'nombre'
        )

material_schema = Material_Schema()
materiales_schema = Material_Schema(many=True)