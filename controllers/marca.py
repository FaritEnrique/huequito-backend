from instancias import conexion
from models.marca import MarcaProductoModel
from flask_restful import Resource, request
from .serializers import MarcaSerializer
from marshmallow.exceptions import ValidationError

class MarcaController(Resource):
    serializador = MarcaSerializer()
    
    def post(self):
        data = request.get_json()
        
        try:
            data_serializada = self.serializador.load(data)
            nueva_marca = MarcaProductoModel(**data_serializada)
            conexion.session.add(nueva_marca)
            conexion.session.commit()
            
            resultado = self.serializador.dump(nueva_marca)
            
            return {
                'message': 'Marca creada exitosamente',
                'content': resultado  
            }
            
        except ValidationError as error:
            return{
                'message': 'Error al crear marca',
                'content': error.messages
            }

    def get(self):
        
        marcas = conexion.session.query(MarcaProductoModel).all()
        
        return {
            'message': 'La data se ha generado correctamente',
            'content':  self.serializador.dump(marcas, many=True)
        }