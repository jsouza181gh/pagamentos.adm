from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

#git add .
#git commit -m "Texto do commit"
#git push -u origin "branch"