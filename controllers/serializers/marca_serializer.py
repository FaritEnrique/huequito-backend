from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import MarcaProductoModel

class MarcaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = MarcaProductoModel
        include_relationships = True
        load_instance = True
    
    
    