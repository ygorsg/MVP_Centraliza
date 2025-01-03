import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configuração do Flask e do SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Definição dos modelos (Tarefa e Subtarefa)
class Tarefa(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    descricao = db.Column(db.String(500))
    subtarefas = db.relationship('Subtarefa', backref='tarefa')

class Subtarefa(db.Model):
    __tablename__ = 'subtarefas'
    sub_id = db.Column(db.Integer, primary_key=True)
    sub_nome = db.Column(db.String(64), unique=True)
    tarefa_id = db.Column(db.Integer, db.ForeignKey('tarefas.id'))


# Aqui começa a definição de rotas
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/visualizar_tarefas', methods=['GET'])
def visualizar_tarefas():
    tarefas = Tarefa.query.all()
    return render_template('visualizar_tarefas.html', tarefas=tarefas)

@app.route("/pomodoro")
def home():
    return render_template("pomodoro.html")

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

# Inicialização do Banco de Dados e Execução do Servidor
if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)