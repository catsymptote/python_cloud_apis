# Python API

Inspired by [this YouTube video](https://youtu.be/qbLc5a9jdXo) by Caleb Curry.


## Components of an API system
```
+---------+----------+----------+
| Server  |  Medium  | Client   |
+---------+----------+----------+
| Backend |  Files   | Frontend |
| Python  |  JSON    | JS       |
+---------+----------+----------+
```

## Endpoints:
* /drinks: Gets all the drinks
* /drinks/<id>: Gets a specific drink (by id)

E.g. xyz.com/drinks/5
Or api.xyz.com/drinks/5


api.cocktails.com/drinks/search


## HTTP Methods
```
+---------------+--------+------+--------+--------+
| Abbreviation  |   C    |   R  |   U    |   D    |
+---------------+--------+------+--------+--------+
| Method        | Create | Read | Update | Delete |
| REST command  | POST   | GET  | PUT    | DELETE |
+---------------+--------+------+--------+--------+
```

## How to consume API
Can consume the API in Python (see `consume_API.py`), or using Postman.


## How to create API
1. Create the file shown in the `launch_API.py` file.

2. Install `flask` by running `pip install flask`.

3. Run the following three commands (but replace `app_name` with the name of your application):

```
export FLASK_APP=app_name.py
export FLASK_ENV=development
flask run
```

4. Open the link in the browser (see terminal output to find the link).

This accesses the `GET` method we created/copied.

## Post
Use Postman to send a POST request:

```JSON
{
    "name": "Lisa"
}
```

The return should be a JSON object containing the id of the element.

```JSON
{
    "id": 3
}
```

## With database
Copy the code from `db_API.py`.
Open a Python terminal and run

```python
from app_name import db  # app_name is the 'export FLASK_APP=...'. This will give your some warnings, but just ignore them.

db.create_all()

# These depend on the class implementation.
from app_name import Drink
drink = Drink(name="Grape Sode", description="Nommie")
drink
```

Add to the database with:

```python
db.session.add(drink)
db.session.commit()
```

Query the database

```python
Drink.query.all()
```
