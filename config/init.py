import json
from flask import Flask, render_template  
from flask_sqlalchemy import SQLAlchemy


# this is for getting the secret key
with open('config.json') as f:
    config = json.load(f)

# creating an instance of Flask as our app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = config['secret_key']

# creating database connection variable
db = SQLAlchemy()
db.init_app(app)


from config import routes
