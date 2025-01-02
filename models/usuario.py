from instancias import conexion
from sqlalchemy import Column, types
from enum import Enum

class TipoUsuario(Enum):
    ADMIN = 'ADMIN',
    EMPLEADO = 'EMPLEADO'

class Usuario(conexion.Model):
    __tablename__ = "usuarios"
    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text, nullable=False)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=False)
    tipoUsuario = Column(type_=types.Enum(TipoUsuario), default= TipoUsuario.EMPLEADO)
    
    def __repr__(self):
        return (
            f"<Usuario(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', "
            f"correo='{self.correo}', tipoUsuario='{self.tipoUsuario.name}')>"
        )