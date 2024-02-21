import psycopg2
from flask import jsonify
import os

def get_db_connection():
    try:
        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

def insert_file(filename, file_content):
    connection = get_db_connection()
    if connection is None:
        return False, "Error de conexión a la base de datos"

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO \"public\".\"File\" (name_file, content) VALUES (%s, %s)", (filename, file_content))
        connection.commit()
        cursor.close()
        return True, "Archivo guardado en la base de datos correctamente"
    except psycopg2.Error as e:
        print("Error al guardar el archivo en la base de datos:", e)
        return False, "Error al guardar el archivo en la base de datos"
    finally:
        if connection is not None:
            connection.close()

def get_user(username):
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, pass FROM public.\"Users\" WHERE name = %s", (username,))
        user_row = cursor.fetchone()
        cursor.close()
        if user_row is None:
            return jsonify({'message': 'Nombre de usuario incorrecto'}), 401
        return user_row
    except psycopg2.Error as e:
        print("Error al realizar la consulta:", e)
        return None
    finally:
        if connection is not None:
            connection.close()
