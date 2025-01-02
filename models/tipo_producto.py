from instancias import conexion
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TipoProductoModel(conexion.Model):
    __tablename__ = "tipo_producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    
    productos = relationship("ProductoModel", backref="tipo_producto", lazy=True)
    marcas = relationship("MarcaProductoModel", backref="tipo_producto", lazy=True)
    
    def __repr__(self):
        return f"<TipoProducto(id={self.id}, nombre='{self.nombre}')>"