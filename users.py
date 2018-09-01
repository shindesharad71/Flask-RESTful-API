from flask import Flask, jsonify, make_response

def get_users(cursor):
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

def get_user_by_id(cursor, id):
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
