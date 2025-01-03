from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import TipoProductoModel

class TipoProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = TipoProductoModel
        include_relationships = True
        load_instance = True