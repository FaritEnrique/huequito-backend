from instancias import conexion
from sqlalchemy import Column, Integer, String

class TipoProductoModel(conexion.Model):
    __tablename__ = "tipo_producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    