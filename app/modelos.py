from app import app, db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    usuario = Mesario.query.get(int(user_id))
    if usuario:
        return usuario

    usuario = Urna.query.get(int(user_id))
    if usuario:
        return usuario

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    urna = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(128), nullable=False)
    matricula = db.Column(db.String(7), unique=True, nullable=False)
    voto = db.Column(db.Integer, nullable=True)
    votou_quando = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<Aluno %r, UrnaID: %r, VotouQuando: %r>' % self.nome, self.urna, self.votou_quando
    
class Mesario(db.Model, UserMixin):
    __tablename__ = 'mesarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    urna = db.Column(db.Integer, nullable=False)
    login = db.Column(db.String(128), nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    votou_quando = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def verificar_senha(self, senha):
        return self.senha == senha

    def __repr__(self):
        return '<Mesario %r, UrnaID: %r, Nome: %r>' % self.login, self.urna

class Candidato(db.Model):
    __tablename__ = 'canditados'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    urna = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(128), nullable=False)
    imagem = db.Column(db.String(128), nullable=False)
    numero = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Candidato %r, UrnaID: %r, Numero: %r>' % self.nome, self.urn, self.numero

class Urna(db.Model, UserMixin):
    __tablename__ = 'urnas'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    quantidade_votos = db.Column(db.Integer, nullable=False, default=0)
    ultimo_acesso = db.Column(db.DateTime, nullable=False)
    ultimo_voto = db.Column(db.DateTime, nullable=False)
    login = db.Column(db.String(128), nullable=False)
    senha = db.Column(db.String(128), nullable=False)

    def verificar_senha(self, senha):
        return self.senha == senha

    def __repr__(self):
        return '<Urna %r, Ultimo_acesso: %r, Ultimo_voto: %r>' % self.id, self.ultimo_acesso, self.ultimo_voto
