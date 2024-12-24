from instancias import conexion
from sqlalchemy import Column, Integer, String, ForeignKey


class MarcaProductoModel(conexion.Model):
    __tablename__ = "marca_producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    tipo_producto_id = Column(Integer, ForeignKey('tipo_producto.id'))