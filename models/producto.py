from instancias import conexion
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class ProductoModel(conexion.Model):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    precio = Column(Float, nullable=False)
    tipo_producto_id = Column(Integer, ForeignKey('tipo_producto.id'), nullable=False)
    marca_id = Column(Integer, ForeignKey('marca_producto.id'), nullable=False)  # Cambié 'marca.id' a 'marca_producto.id'
    color_id = Column(Integer, ForeignKey('color_producto.id'), nullable=True)  # Cambié 'color.id' a 'color_producto.id'
    
    def __repr__(self):
        return (
            f"<Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})>"
            f", tipo_producto_id={self.tipo_producto_id}, marca_id={self.marca_id}, color_id={self.color_id})>"
        )