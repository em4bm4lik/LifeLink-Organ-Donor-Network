from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.hospital import hospital_bp
    from app.routes.organ import organ_bp
    from app.routes.offer import offer_bp
    from app.routes.request import request_bp
    from app.routes.donation import donation_bp
    from app.routes.dashboard import dash_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(hospital_bp)
    app.register_blueprint(organ_bp)
    app.register_blueprint(offer_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(dash_bp)

    return app
