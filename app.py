from flask import Flask
from flask_migrate import Migrate
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from models import *
from flask_restful import Api
from controllers.tipo_producto import TiposProductosList
from controllers.marca import MarcaController

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:FeT451125@localhost:5432/db_huequito'

conexion.init_app(app)
migrate = Migrate(app, conexion)

api = Api(app)

api.add_resource(TiposProductosList, "/tipo-productos")
api.add_resource(MarcaController, "/marcas")

if __name__ == '__main__':
    app.run(debug=True)