# SYSACAD
-------------------------
DESCRIPCIÓN DEL PROYECTO
-------------------------
Sysacad es un sistema académico desarrolado con Python (Flash) y PostgreSQL, para la gestión académica universitaria. Permite administrar la información deuniversidades, planes de estudiom certificados académicos, alumnos y más. El proyecto(sistema, aplicación) tiene una arquitectura modular, donde cada módulo(modelos, servicios, repositorios, mappings) está separado, de acuerdo
a su responsabilidad. También incluye tests automáticos,

-------------------------
REQUERIMIENTOS
-------------------------
    .Python 3.11+
    .PostgreSQL (para la base de datos)
    .Docker y Docker Compose (opcional, para levantar el entorno en contenedores)
Las dependencias de Python necesarias para el proyecto estan en el archivo
*requirements.txt*, para instalarlas hay que ejecutar en la terminal:
*pip install -r requirements.txt*

-------------------------
EJECUCIÓN DEL PROYECTO PARA TESTS
-------------------------
1. Clonar el repositorio
git clone <https://github.com/Elwilsonic/SYSCAD.git>
cd SYSCAD (entrar al proyecto en Visual)

2. Crear y activar un entorno virtual
python -m venv venv
Despues de hacer eso, hay que hacer lo siguiente:
PARA WINDOWS
.\venv\Scripts\activate
PARA LINUX/MAC
source venv/bin/activate
En el caso de no funcionar, puede ser que la política de ejecución esté bloqueando scripts. Para ese caso, ejecuten lo siguiente:
*Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process*
Luego vuelven a intentar *.\venv\Scripts\activate*

3. Instalar dependencias
pip install -r requirements.txt

4. Verificar que el archivo .env esté en el proyecto, ya está configurado, no tienen que hacer cambios.

5. Anter de ejecutar todos los tests, deben tener las bases de datos creadas localmente (DEV_SYSACAD - SYSACAD - TEST_SYSACAD), los tests se ejecutan con ['FLASK_CONTEXT'] = 'testing', por lo tanto solo deben tener creada TEST_SYSACAD, pero mejor creen las tres bases de datos, la explicación está en el archivo *README_BASE DE DATOS.txt* dentro de la carpeta base_de_datos.

6. Para ejecutar solamente los tests, deben hacerlo con *unittest* para las pruebas automáticas, para ejecutar todos los tests, desde la raíz del proyecto, en la terminal ejecutan: *python -m unittest discover -s test -p "test_*.py"*

-------------------------
EJECUCIÓN DEL PROYECTO PARA LA APP
-------------------------
1. Los pasos son exactamente los mismos hasta el punto 5.

2. Instalar la imagen del docker, esto se tiene que hacer en la raíz del
proyecto, ejecutando: *docker build -t flask-sysacad:v1.0.0 .*

3. Una vez hecho lo anterior, hay que entrar a la carpeta docker, con
cd .\docker\ y ahí instalar los contenedores, ejecutando: 
*docker compose up -d*

4. Una vez levantado los contenedores, hay que verificar si están corriendo, se puede hacer de dos formas, entrando a Docker Desktop o ejecutando en la terminal: docker ps.

5. Abrir docker desktop, en el contenedor *estructura-1*, darle a los tres puntos --> Open in terminal (con en contenedor andando), una vez que la terminal se abre, tiene que copiar primero este comando: *flask db init*, luego
tiene que escribir este: *flask db migrate -m "Inicial"* y finalmente tienen
que copiar este comando: *flask db upgrade*.

6. Estando en la carpeta SYSCAD, pueden entrar a la carpeta docker y levantar los contenedores si no los tienen con *docker compose up -d* o levantarlos desde docker desktop.Ya con esto y teniendo la extensión de POSTMAN, pueden simular peticiones HTTP (teniendo los PUT, GET, DELETE, POST).

#NO ES NECESARIO LEVANTAR LA APP CON *python app.py*, cuando hagamos los pasos 5 y 6, ya que al levantar docker, Flask ya esta corriendo dentro del contenedor#

INTEGRANTES:
Batista Martina
Cabeza Florencia
Cardozo Leandro
Carrieri Bruno
Peñalbé Hernán