from instancias import conexion
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey


class ProductoModel(conexion.Model):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    precio = Column(Float, nullable=False)
    tipo_producto_id = Column(Integer, ForeignKey('tipo_producto.id'), nullable=False)
    marca_id = Column(Integer, ForeignKey('marca.id'), nullable=False)
    color_id = Column(Integer, ForeignKey('color.id'), nullable=True)
    
    tipo_producto = relationship("TipoProductoModel", backref="productos")
    marca = relationship("MarcaProductoModel", backref="productos")
    color = relationship("ColorProductoModel", backref="productos")
    
    def __repr__(self):
        return (
            f"<Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})>"
            f"tipo_producto_id={self.tipo_producto_id}, marca_id={self.marca_id}, color_id={self.color_id})>"
        )