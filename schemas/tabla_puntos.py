from utils.ma import ma
from marshmallow import fields

from models.tabla_puntos import Tabla_puntos
from schemas.eco_aprendiz import Ecoaprendiz_Schema

class TablaPuntos_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tabla_puntos
        include_fk = True
        include_relationships = True
        fields = (
            'id_tp',
            'id_aprendiz',
            'ptos_exp',
            'ptos_app',
            'eco_aprendiz'
        )
    
    eco_aprendiz = ma.Nested('Ecoaprendiz_Schema')

tabla_puntos_schema = TablaPuntos_Schema()
tablas_puntos_schema = TablaPuntos_Schema(many=True)