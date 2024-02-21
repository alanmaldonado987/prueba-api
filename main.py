from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import os
import pandas as pd
import jwt
import datetime
from flask_cors import CORS
from db.database import insert_file, get_user
from utils.auth import token_required
from utils.file_utils import allowedFile

app = Flask(__name__)
app.config["Upload_Foder"] = "static/uploads"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app)


resultados_analisis = None

@app.route("/upload", methods=["POST"])
@token_required
def upload(current_user):
    file = request.files["uploadFile"]

    if not allowedFile(file.filename):
        return jsonify({'message': 'Extensión de archivo no permitida'}), 400

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["Upload_Foder"], filename))
    file_path = os.path.join(app.config["Upload_Foder"], filename)

    df = pd.read_excel(file_path)
   
    suma_columna = df['CSMO_NORM_202312'].sum()
    media_columna = df['CSMO_NORM_202312'].mean()
    desviacion_estandar_columna = df['CSMO_NORM_202312'].std()
    mediana = df['CSMO_NORM_202312'].median()
    correlacion = df['CSMO_NORM_202312'].corr(df['CSMO_NORM_202311'])

    global resultados_analisis
    resultados_analisis = {
        "sum2a": suma_columna,
        "desviacion_estandar": desviacion_estandar_columna,
        "media": media_columna,
        "mediana": mediana,
        "correlacion": correlacion,
        "prueba": "prueba"
    }

    with open(file_path, "rb") as f:
        file_content = f.read()

    success, message = insert_file(filename, file_content)
    if not success:
        return jsonify({'message': message}), 500

    return "Archivo guardado en la base de datos correctamente"


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user_row = get_user(username)
    if user_row is None:
        return jsonify({'message': 'Usuario no encontrado'}), 401

    stored_password = user_row[1] 
    if password != stored_password:
        return jsonify({'message': 'Contraseña incorrecta'}), 401
        
    #JWT
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200



@app.route("/data2", methods=["GET"])
def get_data():
    if resultados_analisis is None:
        return jsonify({"message": "No se ha cargado ningún archivo aún"}), 404
    
    print(resultados_analisis)
    return jsonify(resultados_analisis)

if __name__ == "__main__":
    app.run(debug=True)
