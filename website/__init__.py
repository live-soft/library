from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'

    from .controllers.home import home
    from .controllers.single import single

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(single, url_prefix='/')

    return app