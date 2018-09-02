from flask import Flask, jsonify, make_response, request
import db
import jwt
import users

app = Flask(__name__)

cursor, conn = db.connection(app)


@app.route('/')
def index():
    return make_response(jsonify({'message': 'Its working!'}), 200)


@app.route('/users', methods=['GET', 'POST'])
def getAllUsers():
    return users.get_users(cursor, conn, request)


@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def singleUser(id):
    return users.get_user_by_id(cursor, conn, request, id)


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'flask-api'
    app.run(port=8080)
