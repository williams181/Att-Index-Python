from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

# Declara o flask app
app = Flask(__name__, template_folder='./templates')

app.secret_key = 'ABCDDD123'

# estabelece as configurações com o mysql 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://william:1234will@db/myflask'

db = SQLAlchemy(app)

# define os campos da tabela funcionario
class Funcionario(db.Model):
    __tablename__='funcionario'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(500))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
       
db.create_all()

# exibe a pagina inicial.
@app.route('/')
def index():
    
    return render_template('index.html')

# exibi a tela de cadastro de funcionario
@app.route("/cadastrar")
def cadastrar():

    return render_template("cadastro.html")

# cadastro de funcionario
@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")

        if nome and email:
            f = Funcionario(nome, email)
            db.session.add(f)
            db.session.commit()

    return redirect(url_for("index"))

# lista de funcionarios
@app.route("/lista")
def lista():
    funcionarios = Funcionario.query.all()
    return render_template("lista.html", funcionarios=funcionarios)

# exclui um funcionario com base em seu identificador
@app.route("/excluir/<int:id>")
def excluir(id):
    funcionario = Funcionario.query.filter_by(_id=id).first()

    db.session.delete(funcionario)
    db.session.commit()

    funcionarios = Funcionario.query.all()

    return render_template("lista.html", funcionarios=funcionarios)

# atualiza os dados do usuario com base em um identificador
@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    funcionario = Funcionario.query.filter_by(_id=id).first()

    if request.method == 'POST':
        nome = request.form.get("nome")
        email = request.form.get("email")

        if nome and email:
            funcionario.nome = nome
            funcionario.email = email

            db.session.commit()

            return redirect(url_for("lista"))

    return render_template("atualizar.html", funcionario=funcionario)

# executa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
