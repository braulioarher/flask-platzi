from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login  import LoginManager
from .config import Config
from .auth import auth
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__) #Creamos una nueva instacia pasandole el nombre de la aplicacion
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)

    #Antes de regustrar los blueprints se inicializa la aplicacion
    login_manager.init_app(app)

    #Se agrega nuestra blueprint al entorno de la aplicacion
    app.register_blueprint(auth)

    return app