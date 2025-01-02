from instancias import conexion
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class MarcaProductoModel(conexion.Model):
    __tablename__ = "marca_producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    tipo_producto_id = Column(Integer, ForeignKey('tipo_producto.id'), nullable=False)
    
    tipo_producto = relationship("TipoProductoModel", backref="marcas")
    
    def __repr__(self):
        return f"<MarcaProducto(id={self.id}, nombre='{self.nombre}', tipo_producto_id={self.tipo_producto_id})>"