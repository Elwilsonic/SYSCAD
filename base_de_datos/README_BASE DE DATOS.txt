README - Configuración de la Base de Datos para el Proyecto Sysacad
===================================================================

Este documento explica los pasos necesarios para crear y configurar 
la base de datos del proyecto Sysacad utilizando PostgreSQL y SQL Shell (psql).

REQUISITOS PREVIOS
------------------
- PostgreSQL instalado
- Python y entorno virtual configurado
- Proyecto clonado con entorno `venv` activado

PASOS PARA CREAR LAS BASES DE DATOS
-----------------------------------

1. **Abrir SQL Shell (psql):**

   Al abrir SQL Shell, crear el usuario si no existe (SOLO NI LO LO HABÍAS CREADO ANTES)
   ```
   CREATE USER pprats WITH PASSWORD 'naranja';
   ```

2. **Crear las bases de datos necesarias:**

   En la consola de `psql`, ejecutá:

   ```sql
   CREATE DATABASE "DEV_SYSACAD" OWNER pprats;
   CREATE DATABASE "TEST_SYSACAD" OWNER pprats;
   CREATE DATABASE "SYSACAD" OWNER pprats;
   ```

   Usá punto y coma (`;`) al final de cada línea.

3. **Verificar que las bases fueron creadas:**

   Ejecutá este comando para listar todas las bases:

   ```sql
   \l
   ```

   Deberías ver `DEV_SYSACAD`, `TEST_SYSACAD` y `SYSACAD` en la lista.


5. **Verificar conexión desde la aplicación:**

   ejecutar los tests de conexión:

   ```
   python tests/test_db.py
   ```

   Debería mostrar:
   ```
   .
   ----------------------------------------------------------------------
   Ran 1 test in X.XXXs

   OK
   ```

6. **Crear las tablas automáticamente (si aplica):**

   Los tests se encargan de crear y borrar las tablas antes y después de correr, usando `db.create_all()`.

   También podés crear las tablas manualmente desde la consola de Flask:

   ```
   flask shell
   >>> from app import db
   >>> db.create_all()
   ```

NOTAS ADICIONALES
------------------
- Asegurate de tener instalado el driver de PostgreSQL para Python:
  ```
  pip install psycopg2-binary
  ```