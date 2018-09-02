from subprocess import call
import os

print('checking for required packages')
try:
    import flask
    import jwt
    print('required packages found')
except ImportError:
    os.system('pip3 install -r requirements.txt')
    print('required packages installed')
    print("you need to install packages by running pip3 install -r requirements.txt before continuing")
