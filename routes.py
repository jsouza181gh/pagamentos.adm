from main import app
from flask import render_template, redirect, url_for

@app.route('/')
def homepage():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def test():
    return render_template('cadastro.html')