# -*- coding: utf-8 -*-

from flask import Flask,jsonify,request
from flask_cors import CORS
import json
import random
from decimal import Decimal
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# define global variables
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.usage = 0
        self.is_login = True

users = []

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        username = data['username']
        password = data['password']
        for user in users:
            if user.username == username:
                user.password = password
                return json.dumps(user.__dict__)
        #如果没有就注册
        user = User(username, password)
        users.append(user)
        return json.dumps(user.__dict__)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        username = data['username']
        for user in users:
            if user.username == username:
                randusage = random.randint(1,10)+random.random()
                user.usage+=randusage
                user.usage = round(user.usage,2)#保留两位小数
                return json.dumps(user.__dict__)
        return json.dumps(user.__dict__)

if __name__ == '__main__':
    app.run()
