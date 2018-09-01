import jwt

secret = 'flask-api'
hashing = 'HS256'

def encode_jwt(id):
    return jwt.encode({'id': id}, secret, algorithm=hashing)

def decode_jwt(encoded):
    return jwt.decode(encoded, secret, algorithms=[hashing])