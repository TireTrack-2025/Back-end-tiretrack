from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Veiculo
from app.schemes import VeiculoSchema

bp = Blueprint("veiculos", __name__)
veiculo_schema = VeiculoSchema()
veiculos_schema = VeiculoSchema(many=True)

# GET /api/veiculos/ping
@bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "API de Veículos funcionando 🚗"})


# POST /api/veiculos  -> Cadastrar novo veículo
@bp.route("/", methods=["POST"])
def create_veiculo():
    data = request.get_json()
    errors = veiculo_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    veiculo = Veiculo(**data)
    db.session.add(veiculo)
    db.session.commit()

    return veiculo_schema.jsonify(veiculo), 201


# GET /api/veiculos  -> Listar todos os veículos
@bp.route("/", methods=["GET"])
def get_veiculos():
    veiculos = Veiculo.query.all()
    return veiculos_schema.jsonify(veiculos), 200


# GET /api/veiculos/<id>  -> Buscar veículo por ID
@bp.route("/<int:id>", methods=["GET"])
def get_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    return veiculo_schema.jsonify(veiculo)


# PUT /api/veiculos/<id>  -> Atualizar veículo
@bp.route("/<int:id>", methods=["PUT"])
def update_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    data = request.get_json()
    errors = veiculo_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(veiculo, key, value)

    db.session.commit()
    return veiculo_schema.jsonify(veiculo)


# DELETE /api/veiculos/<id>  -> Remover veículo
@bp.route("/<int:id>", methods=["DELETE"])
def delete_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return jsonify({"message": "Veículo deletado com sucesso"}), 200
