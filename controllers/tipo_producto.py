from instancias import conexion
from models.tipo_producto import TipoProductoModel
from flask_restful import Resource, request

class TiposProductosList(Resource):
    def get(self):
        data = conexion.session.query(TiposProductosList)
        return {
            'message': 'La data se ha generado correctamente'
        }

class TipoProductoPost(Resource):
    def post(self):
        data = request.get_json()
        