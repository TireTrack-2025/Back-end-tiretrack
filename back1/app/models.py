from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_empresa = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(20), unique=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)

class PerfilAcesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil_acesso.id'), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    perfil = db.relationship('PerfilAcesso')
    empresa = db.relationship('Empresa')

    def set_password(self, password):
        self.senha_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha_hash, password)

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(20), unique=True, nullable=False)
    modelo_veiculo = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer)
    quilometragem_atual = db.Column(db.Integer, default=0)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    empresa = db.relationship('Empresa')

class ModeloPneu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    dimensao = db.Column(db.String(50))
    limite_recapeamentos = db.Column(db.Integer, default=0)

class Pneu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_serie = db.Column(db.String(100), unique=True, nullable=False)
    modelo_pneu_id = db.Column(db.Integer, db.ForeignKey('modelo_pneu.id'))
    status_atual = db.Column(db.Enum('em_estoque','em_uso','em_manutencao','descartado'), default='em_estoque')
    data_aquisicao = db.Column(db.Date)
    quilometragem_total_acumulada = db.Column(db.Integer, default=0)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    modelo = db.relationship('ModeloPneu')
    empresa = db.relationship('Empresa')

class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    modelo = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quilometragem_atual = db.Column(db.Integer, nullable=False, default=0)

    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)

    def __repr__(self):
        return f"<Veiculo {self.placa}>"
