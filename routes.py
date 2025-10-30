from main import app
from crud import buscarFornecedor
from flask import render_template, redirect, url_for

@app.route('/')
def homepage():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/api/<idFornecedor>')
def api(idFornecedor):
    return buscarFornecedor(idFornecedor)