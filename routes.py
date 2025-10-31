from main import app
from crud import buscarFornecedor, criarFornecedor
from flask import render_template, redirect, url_for, request

@app.route('/')
def homepage():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    dadosFormularioCadastro = request.form
    if request.form.get('submit_button') == 'enviar':
        criarFornecedor(
            dadosFormularioCadastro['nome'],
            dadosFormularioCadastro['cnpj'],
            dadosFormularioCadastro['telefone'],
            dadosFormularioCadastro['email'],
            dadosFormularioCadastro['senha']
            )
        
        print(dadosFormularioCadastro['nome'])
        
    return render_template('cadastro.html')

@app.route('/api/<idFornecedor>')
def api(idFornecedor):
    return buscarFornecedor(idFornecedor)