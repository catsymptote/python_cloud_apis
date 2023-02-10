from flask import Flask, request

app = Flask(__name__)


CONTACTS = [{"name": "Paul"}, {"name": "Mary"}, {"name": "John"}]


@app.route('/')
def hello():
    return 'Hello Flask!'


@app.route('/contacts')
def get_contacts():
    return CONTACTS


@app.route('/contacts/<id>')
def get_contact(id):
    return CONTACTS[int(id)]


@app.route('/contacts', methods=['POST'])
def update_contact():
    name = request.json['name']
    contact = {"name": name}
    CONTACTS.append(contact)

    id = len(CONTACTS) - 1
    return {'id': id}


@app.route('/contacts/<id>', methods=['DELETE'])
def delete_contact(id):
    del CONTACTS[int(id)]
    return  {'id': id}
