from flask import Flask
from sqlalchemy import true
from user import user_api
from project import project_api
from flask_cors import CORS
app = Flask(__name__)

app.register_blueprint(user_api, url_prefix='/user')
app.register_blueprint(project_api, url_prefix='/project')
CORS(app)
if __name__ == '__main__':
   app.run()