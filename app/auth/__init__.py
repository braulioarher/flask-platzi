from flask import Blueprint

#Creamos un nuevo blueprint con nombre 'auth' y prefijo '/auth' lo que significa que todas las rutas que inicien con '/auth'
# seran redirigidas a este blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views