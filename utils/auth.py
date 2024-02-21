# auth.py
from functools import wraps
from flask import request, jsonify
from flask import current_app as app
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token_parts = request.headers['Authorization'].split()
            if len(token_parts) == 2:
                token = token_parts[1]

        if not token:
            return jsonify({'message': 'Token faltante'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
