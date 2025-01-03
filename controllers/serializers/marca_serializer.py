from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import MarcaProductoModel

class MarcaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = MarcaProductoModel
    
    
    