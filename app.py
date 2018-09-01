from flask import Flask, jsonify, make_response
from flaskext.mysql import MySQL

app = Flask(__name__)


def connection():
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'shindesharad71'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234567890'
    app.config['MYSQL_DATABASE_DB'] = 'flask71'
    app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    return cursor

cursor = connection()


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


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)
