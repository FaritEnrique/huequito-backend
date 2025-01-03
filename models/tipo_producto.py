from instancias import conexion
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TipoProductoModel(conexion.Model):
    __tablename__ = "tipo_producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<TipoProducto(id={self.id}, nombre='{self.nombre}')>"
    
    marcas_intermedios = relationship("MarcaTipoProductoModel", back_populates="tipo_producto")
    marcas = relationship("MarcaProductoModel", secondary="marca_tipo_producto", back_populates="tipos")