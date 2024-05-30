from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from routes import *

@app.route('/')
def index():
    solicitudes = Solicitud.query.all()
    return render_template('index.html', solicitudes=solicitudes)


if __name__ == "__main__":
    app.run(debug=True)
