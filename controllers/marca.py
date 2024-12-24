from instancias import conexion
from models.marca import MarcaProductoModel
from flask_restful import Resource
from flask import request

class MarcasList(Resource):
    def get(self):
        data = conexion.session.query(MarcaProductoModel).all()
        return {
            'message': 'La data se ha generado correctamente'
        }