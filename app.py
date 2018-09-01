from flask import Flask, jsonify, make_response
import db

app = Flask(__name__)

cursor = db.connection(app)

@app.route('/')
def index():
    return make_response(jsonify({'message': 'Its working!'}), 200)


@app.route('/users')
def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        all_users = []
        for i in users:
            tmp_user = {
                'id': i[0],
                'email': i[1],
                'name': i[2],
                'contact': i[3]
            }
            all_users.append(tmp_user)
        return make_response(jsonify(all_users), 200)
    else:
        return make_response(jsonify({'message': 'Its something went wrong'}), 400)


@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    cursor.execute('SELECT * FROM users WHERE id = '+id)
    user = cursor.fetchone()
    if user:
        user = {
            'id': user[0],
            'email': user[1],
            'name': user[2],
            'contact': user[3]
        }
        return make_response(jsonify(user), 200)
    else:
        return make_response(jsonify({'message': 'User not found'}), 200)


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'flask-api'
    app.run(port=8080)
