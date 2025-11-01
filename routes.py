from main import app
from crud import *
from flask import render_template, redirect, url_for, request

@app.route('/')
def mainPage():
    return redirect(url_for('login'))

@app.route('/homepage')
def homepage():
    return "Logado"

@app.route('/login', methods=['GET', 'POST'])
def login():
    dadosFormularioLogin = request.form
    if request.form.get('submit_button') == 'enviar':
        print(dadosFormularioLogin['username'])
        print(dadosFormularioLogin['password'])
        return redirect(url_for('homepage'))
    
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
        return redirect(url_for('login'))
        
    return render_template('cadastro.html')

@app.route('/api/<idFornecedor>')
def api(idFornecedorRecebido):
    return buscarFornecedor(idFornecedor=idFornecedorRecebido)

@app.route('/db')
def db():
    return exibirFornecedores()