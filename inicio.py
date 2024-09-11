"""
flask = modulo
Flask = Classe
"""

from flask import Flask


"""
app = objeto
Flask( ) = construtor
__name__ = nome da aplicação
"""
app = Flask(__name__)




@app.route('/')

def index():
    return 'Página inicial - Rei do App'

@app.route('/novofuncionario')
def novo_funcionario():
    return 'Cadastro de Novo Funcionário Adicionado'

@app.route('/novocliente')
def novo_cliente():
    return 'Cadastro de Novo Cliente Adicionado'

@app.route('/novoagendamento')
def novo_agendamento():
    return 'Novo Agendamento Adicionado'

@app.route('/login')
def login():
    return 'Login'

@app.route('/logout')
def logout():
    return 'Logout'

app.run(debug=True)

