# API para manejo de archivos

Esta es una API desarrollada en Phyton con Flask que permite cargar archivos de Excel y hacer calculos estadisticos suministrados en una base de datos PostgreSQL para luego ser visualizados en PowerBI.

## Para clonar el proyecto:

```bash
git clone https://github.com/alanmaldonado987/prueba-api.git
```
 
o descargandolo directamente.

## Configuración

Instala las dependencias del proyecto utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Base de Datos

La API trae su base de datos propia construida en PostgreSQl, para cargarla debe restaurar el archivo "bd_prueba" en algun gestor de base de datos, por ejemplo, en pgAdmin. En dicho archivo se encuentra las tablas con la información necesaria para el funcionamiento de la API.

## Y si no tengo un gestor de base de datos?

Si no tiene algún gestor de base de datos puede hacer uso de Postman, una aplicación americana que permite probar API's.

## Como funciona la API?

## Endpoints

La API cuenta con 3 rutas protegidas para ser consumida:

Login: IMPORTANTE!! las rutas están protegidas por lo que se deberá loguear, las credenciales son:
User: alan1
Password: prueba
```bash
http://localhost:5000/login
```

Upload: Al iniciar sesión la API devolverá un token, debe enviarlo en la petición en dado caso de usar postman, de lo contrario, esto se hará automáticamente. En este endpoint se subirá el archivo y se harán los calculos.
```bash
http://127.0.0.1:5000/upload
```

Data: Aquí se podrán ver el resultado de los cálculos.
```bash
http://localhost:5000/data2
```

## Conexión y Visualización de datos en PowerBI 

Para visualizar los resultados obtenidos por la API en powerBI, deberá consumir la API desde este ultimo, con el token y la dirección:
```bash
http://localhost:5000/data2
```
