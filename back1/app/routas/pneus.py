from flask import Blueprint, request, jsonify
from ..models import Pneu
from ..extensions import db
from flask_jwt_extended import jwt_required, get_jwt

bp = Blueprint('pneus', __name__)

def empresa_do_token():
    claims = get_jwt()
    return claims.get('empresa_id')

@bp.route('/', methods=['POST'])
@jwt_required()
def create_pneu():
    data = request.get_json()
    empresa_id = empresa_do_token()
    pneu = Pneu(
        numero_serie=data['numero_serie'],
        modelo_pneu_id=data.get('modelo_pneu_id'),
        data_aquisicao=data.get('data_aquisicao'),
        empresa_id=empresa_id
    )
    db.session.add(pneu)
    db.session.commit()
    return jsonify({"id": pneu.id, "numero_serie": pneu.numero_serie}), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def list_pneus():
    empresa_id = empresa_do_token()
    pneus = Pneu.query.filter_by(empresa_id=empresa_id).all()
    return jsonify([{"id":p.id, "numero_serie": p.numero_serie, "status": p.status_atual} for p in pneus])
