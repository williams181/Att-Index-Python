from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Declara o flask app
app = Flask(__name__, template_folder='./templates', static_folder='./static')

# estabelece as configurações com o mysql 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@att-index-python_db_1:3306/myflask'

db = SQLAlchemy(app)

# define os campos da tabela funcionario
class Funcionario(db.Model):
    __tablename__='funcionario'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

db.create_all()

# exibe a pagina inicial
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

    print('='*50)
    print('Running...')
    print('='*50)

    app.run(host='0.0.0.0', port=5000, debug=True)
