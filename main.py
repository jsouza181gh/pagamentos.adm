from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

#git add .
#git commit -m "Texto do commit"
#git push -u origin main