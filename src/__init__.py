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

from config import DevelopmentConfig
import db

def create_app(config_class=DevelopmentConfig) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Initialize Flask Extensions here
    # TODO: Use SQlAlchemy Extension to do the Query Database with ORM
    
    # Init the db
    db.init_app(app)
    
    # Register Blueprint here
    from src.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app


# Run in Debug Mode
if __name__ == '__main__':
    app: Flask = create_app()
    app.run(debug=True)