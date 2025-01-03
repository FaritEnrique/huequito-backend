from instancias import conexion
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class MarcaTipoProductoModel(conexion.Model):
    __tablename__ = "marca_tipo_producto"
    marca_id = Column(Integer, ForeignKey("marca_producto.id"), primary_key=True)
    tipo_producto_id = Column(Integer, ForeignKey("tipo_producto.id"), primary_key=True)

    # Relación opcional para facilitar consultas inversas si se desea
    marca = relationship("MarcaProductoModel", back_populates="tipos_intermedios")
    tipo_producto = relationship("TipoProductoModel", back_populates="marcas_intermedios")