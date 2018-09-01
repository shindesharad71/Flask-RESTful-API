from flask import Flask, jsonify, make_response
import db
import users

app = Flask(__name__)

cursor = db.connection(app)


@app.route('/')
def index():
    return make_response(jsonify({'message': 'Its working!'}), 200)


@app.route('/users')
def getAllUsers():
    return users.get_users(cursor)


@app.route('/users/<id>', methods=['GET'])
def singleUser(id):
    return users.get_user_by_id(cursor, id)


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'flask-api'
    app.run(port=8080)
