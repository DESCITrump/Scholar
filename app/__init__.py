    SQLALCHEMY_DATABASE_URI = 'sqlite:///descitrump_scholar.db'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from .models import User, Document, Scholarship
    with app.app_context():
        db.create_all()

    from .routes import main
    from .auth import auth
    from .api import api
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(api, url_prefix='/api')

    return app