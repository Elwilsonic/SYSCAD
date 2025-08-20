from app import create_app
import logging
# Ref: https://docs.python.org/3/library/logging.html
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
app = create_app()

#https://flask.palletsprojects.com/en/stable/appcontext/
app.app_context().push()

if __name__ == '__main__':
    """
    Server Startup
    Ref: https://flask.palletsprojects.com/en/stable/api/#flask.Flask.run
    Ref: Book Flask Web Development Page 9
    """
    app.run(host="0.0.0.0", debug=True, port=5000) #el atributo host es importante porque en este momento
#estamos ejecutando nuestra aplicacion en nuesta computadora pero cuando lo pasemos a un contenedor
#el que va a estar ejecutando sera el contenedor, para que pueda ser accedida desde cualquier
#contenedor la documentacion de flask indica que se debe usar 0.0.0.0 y luego colocamos el puerto
#que el puerto va a ser el que expongamos en el contenedor, luego el debug se recomienda dejarlo en true
#para poder hacer pruebas y ver los cambios en tiempo real.