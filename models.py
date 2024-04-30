from main import db

class Receitas(db.Model):
    id_receitas = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(254))
    valor = db.Column(db.Numeric)
    data = db.Column(db.Date)

class Despesas(db.Model):
    id_despesas = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(254))
    valor = db.Column(db.Numeric)
    data = db.Column(db.Date)

class Guardar(db.Model):
    id_guardar = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(254))
    valor = db.Column(db.Numeric)
    data = db.Column(db.Date)
