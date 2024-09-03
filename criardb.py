from app import app, db
from datetime import datetime

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
    
class Mesario(db.Model):
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

class Urna(db.Model):
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

def adicionar_aluno(urna, nome, matricula, voto=None):
    if (voto): 
        votou_quando = datetime.now()
    else:
        votou_quando = None
    db.session.add(Aluno(urna=urna, nome=nome, matricula=matricula, voto=voto, votou_quando=votou_quando))
    db.session.commit()

def adicionar_mesario(urna, login, senha):
    db.session.add(Mesario(urna=urna, login=login, senha=senha))
    db.session.commit()

def adicionar_candidato(urna, nome, imagem, numero):
    db.session.add(Candidato(urna=urna, nome=nome, imagem=imagem, numero=numero))
    db.session.commit()

def adicionar_urna(login, senha):
    db.session.add(Urna(login=login, senha=senha))
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.metadata.drop_all(bind=db.engine, tables=[Mesario.__table__])
        #db.metadata.drop_all(bind=db.engine, tables=[Urna.__table__])
        Mesario.metadata.create_all(bind=db.engine)
        #adicionar_urna('urna2', '3412232')
        adicionar_mesario(2, 'filipe1', '123')