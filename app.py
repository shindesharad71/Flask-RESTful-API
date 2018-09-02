from flask import Flask, jsonify, make_response, request
import db
import jwt
import users
import config

app = Flask(__name__)

cursor, conn = db.connection(app)


@app.route('/')
def index():
    return make_response(jsonify({
        'message': 'Its working, try other API endpoints!',
        'APIs': [{'url': '/users', 'method': 'GET'},
                 {'url': '/users/<id>', 'method': 'GET'}
                 ]
    }), 200)


@app.route('/users', methods=['GET', 'POST'])
def getAllUsers():
    return users.get_users(cursor, conn, request)


@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def singleUser(id):
    return users.get_user_by_id(cursor, conn, request, id)


if __name__ == '__main__':
    app.debug = config.debug
    app.config['SECRET_KEY'] = config.secret
    app.run(port=config.port)
