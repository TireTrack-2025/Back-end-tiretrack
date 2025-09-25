from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Usuario, PerfilAcesso, Empresa
from flask_jwt_extended import create_access_token
from datetime import timedelta

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = Usuario.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"msg":"Credenciais inválidas"}), 401
    additional = {"perfil": user.perfil.nome, "empresa_id": user.empresa_id}
    access_token = create_access_token(identity=user.id, additional_claims=additional, expires_delta=timedelta(hours=8))
    return jsonify(access_token=access_token)
