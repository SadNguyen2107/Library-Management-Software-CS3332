"""
* __init__.py: Central Function
Hold code for your Flask factory function, 
which is a function you’ll use to set and create the Flask application instance 
where you link all your Flask blueprints together.

? __init__.py: 
* Central Function in which all your Flask Blueprints are combined into 1 Application
* --> Create different Flask application instances for different purposes with different configurations
* Ex: Create a Flask application instance for testing 
* Ex: Create a Flask application instance with proper configurations
"""

from flask import Flask
from flask_cors import CORS

from config import ProductionConfig
from src.extensions import (
    db,
    login_manager,
    mail,
)

import commands


def create_app(config_class=ProductionConfig) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    # Import CORS
    CORS(app=app)

    #? Initialize Flask Extensions here
    #? =====================================================================
    # Add Mail extension
    mail.init_app(app)
    
    # Add SQLAlchemy extension
    db.init_app(app)

    # Add Authentication
    login_manager.init_app(app)
    
    # Init the commands to interact
    commands.init_app(app)
    
    #? Register Blueprint here
    #? =====================================================================
    # Register Blueprint Main
    from src.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Register Blueprint Book API 
    from src.book import bp as book_bp
    app.register_blueprint(book_bp)
    
    # Register Blueprint User API 
    from src.user import bp as user_bp
    app.register_blueprint(user_bp)

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app


# Run in Debug Mode
if __name__ == '__main__':
    app: Flask = create_app()
    app.run(debug=True)