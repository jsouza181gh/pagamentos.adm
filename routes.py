from crud import *
from main import app
from bcrypt import gensalt, hashpw, checkpw
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
        hashSenha = buscarFornecedor(emailFornecedor=dadosFormularioLogin['username'])
        senha = dadosFormularioLogin['password']
        if checkpw(senha.encode('utf-8'), hashSenha.encode('utf-8')):
            return redirect(url_for('homepage'))
        
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.form.get('submit_button') == 'enviar':
        dadosFormularioCadastro = request.form
        senha = dadosFormularioCadastro['senha']
        confirmacaoSenha = dadosFormularioCadastro['confirmar_senha']
        if senha == confirmacaoSenha:
            salt = gensalt(rounds=10)
            novaSenha = senha.encode("utf-8")
            novaSenha = hashpw(novaSenha, salt)
            novaSenha = novaSenha.decode("utf-8")
            criarFornecedor(
                dadosFormularioCadastro['nome'],
                dadosFormularioCadastro['cnpj'],
                dadosFormularioCadastro['telefone'],
                dadosFormularioCadastro['email'],
                novaSenha
                )
            return redirect(url_for('login'))
        
    return render_template('cadastro.html')

@app.route('/api/<idFornecedor>')
def api(idFornecedor):
    return buscarFornecedor(idFornecedor=idFornecedor)

@app.route('/db/fornecedores')
def tabelaFornecedores():
    return exibirFornecedores()

@app.route('/db/colaboradores')
def tabelaColaboradores():
    return exibirColaboradores()

@app.route('/teste')
def teste():
    return render_template('cadastroTeste.html')