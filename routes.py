from main import app
from crud import buscarFornecedor
from flask import render_template, redirect, url_for, request, Blueprint

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
    data = request.form
    print(data)
    return render_template('cadastro.html')

@app.route('/api/<idFornecedor>')
def api(idFornecedor):
    return buscarFornecedor(idFornecedor)