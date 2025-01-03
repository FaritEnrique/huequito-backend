from instancias import conexion
from models.tipo_producto import TipoProductoModel
from flask_restful import Resource, request
from .serializers import TipoProductoSerializer
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import SQLAlchemyError

class TiposProductosList(Resource):
    serializador = TipoProductoSerializer(many=True)

    def get(self):
        try:
            # Intentamos obtener los tipos de productos
            tipos = conexion.session.query(TipoProductoModel).all()

            # Si la consulta es exitosa, serializamos la data y la retornamos
            return {
                'message': 'La data se ha generado correctamente',
                'content': self.serializador.dump(tipos)
            }

        except ValidationError as error:
            # En caso de que ocurra un error al procesar los datos con el serializador
            return {
                'message': 'Error al procesar los datos de tipos de productos',
                'content': error.messages
            }, 400

        except SQLAlchemyError as error:
            # En caso de que ocurra un error en la consulta a la base de datos
            return {
                'message': 'Error al consultar los tipos de productos en la base de datos',
                'content': str(error)
            }, 500

class TipoProductoPost(Resource):
    serializador = TipoProductoSerializer()

    def post(self):
        data = request.get_json()

        if not data:
            return {
                'message': 'Error al crear tipo de producto',
                'content': 'No se enviaron datos'
            }, 400

        try:
            tipo_producto_data = self.serializador.load(data)
            nuevo_tipo = TipoProductoModel(**tipo_producto_data)
            conexion.session.add(nuevo_tipo)
            conexion.session.commit()
            
            resultado = self.serializador.dump(nuevo_tipo)

            return {
                'message': 'Tipo de producto creado correctamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error al crear tipo de producto',
                'content': error.messages
            }, 400
        except SQLAlchemyError as error:
            return {
                'message': 'Error al guardar en la base de datos',
                'content': str(error)
            }, 500