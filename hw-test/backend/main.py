from flask import Flask,jsonify,request
import json
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

@app.route('/login', methods=['GET', 'POST','OPTION'])
def login():
   return jsonify('hello')

if __name__ == '__main__':
   app.run()