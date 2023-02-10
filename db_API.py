from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date.db'

db = SQLAlchemy(app) 

CONTACTS = [{"name": "Paul"}, {"name": "Mary"}, {"name": "John"}]


class Drink(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'


@app.route("/")
def hello():
    return "Hello Flask!"


@app.route('/contacts')
def get_drinks():
    return CONTACTS


@app.route('/contacts/<id>')
def get_contact(id):
    return CONTACTS[int(id)]
