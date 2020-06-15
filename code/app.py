from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

# Creates Flask app
app = Flask(__name__)
app.secret_key = 'cesar'
# Creates API for app
api = Api(app)

# Allows authentification of users
jwt = JWT(app, authenticate, identity)

# Adss resource and determines how it's accesed
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
