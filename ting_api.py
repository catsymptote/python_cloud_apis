from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/contacts', methods=['POST'])
def update_contact():
    name = request.json['name']
    contact = {"name": name}
    CONTACTS.append(contact)

    id = len(CONTACTS) - 1
    return {'id': id}
