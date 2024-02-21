# API Flask para manejo de archivos y usuarios

Esta es una API desarrollada en Flask que permite cargar archivos de Excel y hacer calculos estadisticos suministrados en una base de datos PostgreSQL.

## Configuración

1. Instala las dependencias del proyecto utilizando el siguiente comando:

```bash
pip install -r requirements.txt


2. En dado caso de tener base de datos propia rellenar el archivo .env ubicado en el directorio raíz del proyecto y rellene las variables de entorno necesarias para la conexión a la base de datos PostgreSQL. Aquí tienes un ejemplo de las variables que podrías definir:

```bash
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=store-carvajal


3. Ejecuta la aplicación Flask utilizando el siguiente comando:

```bash
flask --app main run