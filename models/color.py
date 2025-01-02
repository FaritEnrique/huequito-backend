from instancias import conexion
from sqlalchemy import Column, Integer, String


class ColorProductoModel(conexion.Model):
    __tablename__ = "color_producto"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(30), nullable=False)
    
    def __repr__(self):
        return f"<Color(id={self.id}, descripcion='{self.descripcion}')>"