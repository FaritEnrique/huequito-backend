from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import ColorProductoModel

class ColorSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = ColorProductoModel
        load_instance = True