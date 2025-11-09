from flask import render_template, redirect, url_for, request
from services import validarCadastro, validarLogin
from main import app

@app.route('/')
def mainPage():
    return redirect(url_for('login'))

@app.route('/homepage')
def homepage():
    return "Logado"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        if validarLogin(
            request.form['email'],
            request.form['senha']
        ):
            return redirect(url_for('homepage'))
    

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')
    
    elif request.method == 'POST':
        if validarCadastro(
            'colaborador' in request.form,
            request.form['nome'],
            request.form['cnpj/matricula'],
            request.form['email'],
            request.form['senha'],
            request.form['confirmar_senha'],
        ):
            return redirect(url_for('homepage'))