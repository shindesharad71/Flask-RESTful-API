from flaskext.mysql import MySQL

def connection(app):
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'shindesharad71'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234567890'
    app.config['MYSQL_DATABASE_DB'] = 'flask71'
    app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    return cursor