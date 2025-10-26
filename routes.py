from main import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/teste')
def test():
    return 'Hello, World!'