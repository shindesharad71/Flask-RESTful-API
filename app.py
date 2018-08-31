from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'shindesharad71'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234567890'
app.config['MYSQL_DATABASE_DB'] = 'flask71'
app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchone()
    return jsonify({ 'data': data })


if __name__ == '__main__':
    app.run(debug=True)
