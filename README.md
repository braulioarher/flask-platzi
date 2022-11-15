# Curso de Flask

Para comenzar a trabajar primero debemos de crar un ambiente virtual para esto

    python3 -m venv venv

Despues debemos instalar mediante pip flask pra esto

    pip install flask

Es importante crear un archivo requiremets.txt para saber la dependecias a usarse en este caso agregariamos flask a estas dependencias

Creamos un archivo que se llamara main

Ejecutamos el comando "flask run" para inicializar nuestro servidor

Dentro de la terminal debemos de instanciar una variable que es export FLASK_APP=main.py

Para actualizar automaticamente los cambios echos debemos de activar el modo debug

Se debe de crear una variable en la consola llamada export FLASK_DEBUG=1

## Template con ninja

Un template de flask es un archivo de html que permite renderizar informacion dinamica y estatica en el ejemplo en lugar de regresar una cadena de texto de python se regresa un archivo html

Flask esta por defecto configurado para buscar en una carpeta llamada templates un archivo html

## Macros

Los macros son pequenos pedazos de codigo reutilizables que se repitenen en varias ocaciones de nuestro template

## Configuracion de paginas de error

Cuando el navegador hace un request a la direccion y esta regresa un error por ejemplo el 404 debemos de manejarlo adecuandamente con nuestra aplicacion

Esto se hace por medio de error handler:

            @app.errorhandler(404) #se declara un decorador con el numero del error
            def not_found(error):       #Se declara una funcion que regresa el template a cargar
                return render_template('nombre_template', error = error)

Entonces una vez declarada nuestra funcion podemos crear un archivo html que sera lo que regresara nuestro servidor dependiendo del error que se provoque

## Extenciones de flask. Flask Bootstrap

La extenciones de flask son paqueterias o librerias que le podemos agregar a flask para anadir funcionalidades diferentes

### Bootstrap

Es un framework frontend creado por twitter para generar interfases de usuario primero lo debemos de instalar en nuestro entorno virtual para esto:

            1.- Agregamos flask-bootstrap a nuestros requirements
            2.- Instalamos bootstrap: pip install -r requirements.txt
Para inicializar bootstrap o una extension
            1.- Importamos bootstrap     from flask_bootstrap import Bootstrap
            2.- Instanciamos una variable bootstrap = Bootstrap(app)
Con lo anterior ya podemos utilizar bootstrap se creo una barra de navegacion con estilos de bootstrap pra mas informacion consultar documentacion de bootstrap:
    "https://getbootstrap.com/docs/3.3/components/"

## Configuracion de flask

Para activar el development mode:
            export FLASK_ENV=development
            echo $FLASK_ENV

## Implemetar Flask-Bootstrap y Flask-WTF

WTF es una libreria de pyhton para renderizar forms web para instalarlo lo annadimos a requiements (flask-wtf) para instalarlo:
                - pip install flask-wtf
con esta accion podemos a wtf desde archivos python

## Uso de metodo POST en Flask-WTF

Flas acepta peticiones GET por defecto y por ende no debemos declarla en nuestras rutas

Pero cuando necesitamos hacer una peticion POST al enviar un formularion debemos declararla de la siguiente manera, como en este ejemplo:

        @app.route('/platzi-post', methods=['GET', 'POST'])

Debemos declararle ademas de la peticion que queremos, GET, ya que le estamos pasando el paramentro methos para que acepte solo y unicamente las peticiones que estamos declarando

De esta forma, al actualizar el navegador ya podremos hacer la petición POST a nuestra ruta deseada y obtener la respuesta requerida.

## Flask Factory

Flask factory es una herramienta que nos ayuda a mejorar la estructura de nuestro proyecto en esta utilidad creamos in archivo llamado __init__.py para que se cree un paquete dentro de este archivo creamos una funcion que se llama create_app la cual regresa un objeto applicacion

## Blueprints flask

Un blueprint es como una pequena aplicacion de flask que tiene rutas y templates, para crear un blueprint lo podemos crear desde un nuevo directorio para esto podemos crear dentro de nuestra carpeta proyecto una nueva que se llame auth la cual contendra nuestra blueprint

Dentro de esta carpeta creamos el archivo __init__.py donde inicializamos una variable para definir el blueprint esta con la clase Blueprint importada desde flask

Tambien se crea un archivo views que sera el lugar donde crearemos las viewfunctions las cuales ayudaran a por ejemplo renderizar un archivo html o administrar las peticiones que vengan desde el cliente para crear la ruta simplemente usamos el decorador @auth.route('/login')

Los archivos html los podemos registrar como siempre dentro de la carpeta templates

Como se vio un Blueprint es una serie de rutas que integramos dentro de nuestra aplicacion para modularizar nuestra aplicacion en pequenas aplicaciones por ejemplo de autentificacion o un dashboard

## Base de datos

En este proyecto se usa google firestore que es una base de datos orientada a documentos para poder usarlo debemos de instalar el paquete googlecloudsdk para esto debemos de hacer lo siguiente

Se crea una cuenta en google cloud y despues creamos un proyecto dentro del proyecto creamos una base de datos de tipo firestore

Creada nuestra base de datos en fire store de Google Cloud podemos installar en google cloud en nuestro sistema operativo y autenticar despues creamos dentro de nuestro proyecto un archivo que se llame firestore_service.py desde donde inicamos nuestro cliente firestore donde podremos crear funciones que nus ayuden a mandar peticiones a nuestra base de datos

## Consultando a la base de datos

Como se vio creamos una view function la cual renderizaba una lista de cosas por hacer ahora la intencion consultar los todos a la base datos y desplegar la lista en la hello function una vez que hayamos autenticado mediante username y password emtonce dentro de nuestra funcion hello haremos la consulta usando las funciones importadas desde el archivo firestore_service.py

## Authenticacion de usuarios: Login

Para comenzar a trabajar con el login de Flask necesitamo el paquete flask-login la cosar por hacer son:

    1.- Implementar un login manager el cual va inicializar la app y cargar al usuario

Lo anterior lo hacemos dentro del archivo __init__.py de nuestro proyecto

## Crear nuevos usuarios: Sign up

En esta clase se creo una view function dentro de views en la blueprinth de auth donde mediate un formulario que se reciclo de la funcion login se usa para agregar un nuevo usuario los pasos son los siguientes:

    1.- Renderiza el formulario
    2.- Cundo se presiona el boton de submit manda el metodo post y gurda la informacio de usuario y contrasena
    3.- Verifica que el usuario no existe en la base de datos
    4.- Si no existe en la base de datos  se hashea la contrasena y se ejecuta el metodo user_put la cual agrega el usuario a la base de datos
    5.- Por ultiomo se crea una instancia l metodo UserModel para de esta forma mantener iniciada la sesion usando el metodo login_user de la libreria Flask-Login y se renderia la pagina de inicio

## Crear tareas

Para crear tareas las cuales la pueda agregar cualquier ususario de necesita hacer lo siguientes:

    1.- Crear una nueva forma
    2.- Se agrega la forma a nuestro documento de hello html
    3.- Modificamos nuestra view function para aceptar metodo post
    4.- Agregamos una nueva funcion para anadir elementos a la base de datos en el archivo firestore_service.py
    5.- Inluimos dicha funcion en nuestra view function y redirigimo a hello donde se veran los cambios 

## Borrar tareas

Para borrar tareas las pasos a seguir son:

    1.- Crear una forma en forms.py con un submit field
    3.- Crear una funcion la cual borra el todo en la base de datos en el archivo firestoe_service.py
    4.- Agregar un viewfunction la cual acepta un metodo post que al presionar submit ejecuta la funcion todo_delete() y redirecciona hello
    5.- En la funcion hello se pasa el formulario y en macros se ajusta para anadir el boton a cada elemento de los todo

## Editar tareas

Para modificar y editar tareas:

    1.- Se crea una funcion dentro de firestore_service.py la cual actualiza el valor de donde hacienco invirtiendo el estado de la tarea
    2.- Se crea una formulario similar al de borrar tareas este se llama update form
    3.- Dentro de main se actualiza la view function hello donde se le pasa el formulario de update form
    4.- Se agrega el formulario a los macros y al html de hello
    5.- Se crea una funcion dentro de main.py la cual redirige la peticion post a la funcion de editar en el archivo de firestore_service.py

## Deploy a produccion con App Engine

En este caso se realizara el deploy a una plataforma que se llama app engine la cual es un servicio de google cloud para esto hacemos lo siguiente

        1.- Creamos un nuevo proyecto en google cloud que sera el de produccion
        2.- Desde nuestra consola cambiamos el projecto con el comando:
                gcloud config set project platzi-flask-production-368720
        3.- Creamos en nuestro pructi junto al archivo main.py un archivo llamaco app.yaml que simplemente dira runtime: python37
        4.- Ejecutamos el comando siguiente para cargar la aplicacion
                gcloud app deploy app.yaml
        5.- En caso de que pida iniciar la API hacerlo para que permita cargar
        6.- Iniciamos el servicio de firestore en nuestro proyecto
        7.- Una vez subida nuestra app ejecutamos el comando para poder verla en linea
                gcloud app browse

Listo con los pasos anteriores vimos como deplay nuestra applicacion.

Para hacer deploy de otra version el comando es:

        gcloud app deply app.yaml --version
