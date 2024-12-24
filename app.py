from flask import Flask
from flask_migrate import Migrate
from instancias import conexion
from models import *
from flask_restful import Api
from controllers.tipo_producto import TiposProductosList
from controllers.marca import MarcasList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:FeT451125@localhost:5432/db_huequito'

conexion.init_app(app)
migrate = Migrate(app, conexion)

api = Api(app)

api.add_resource(TiposProductosList, "/tipo-productos")
api.add_resource(MarcasList, "/marcas")

if __name__ == '__main__':
    app.run(debug=True)