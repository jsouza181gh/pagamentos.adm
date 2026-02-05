from flask import render_template, redirect, url_for, request, flash
from services import validarCadastro, validarLogin
from main import app

@app.route('/')
def mainPage():
    return redirect(url_for('login'))

@app.route('/homepage')
def homepage():
    pagamentos = ["Pagamento 1", "Pagamento 2", "Pagamento 3"] # Exemplo de dados
    return render_template('home.html', usuario="Usuário", pagamentos=pagamentos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        if validarLogin(
            request.form['email'],
            request.form['senha']
        ):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Erro no login. Verifique suas informações e tente novamente.', 'danger')
            return redirect(url_for('login'))
    

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
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Erro no cadastro. Verifique os dados e tente novamente.', 'danger')
            return redirect(url_for('cadastro'))