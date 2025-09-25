from .extensions import ma
from .models import Pneu

class PneuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pneu
        load_instance = True

from marshmallow import Schema, fields

class VeiculoSchema(Schema):
    id = fields.Int(dump_only=True)
    placa = fields.Str(required=True)
    modelo = fields.Str(required=True)
    ano = fields.Int(required=True)
    quilometragem_atual = fields.Int()
    empresa_id = fields.Int(required=True)
