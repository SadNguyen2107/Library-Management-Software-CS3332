"""
Configuration File:

!Why need it?
* Separating your application settings from the rest of the application
* Making changing settings easier

? Will configure:
* SECRET KEY
* SQLALCHEMY DATABASE URI 
* SQLALCHEMY_TRACK_MODIFICATIONS
"""

import os
from dotenv import dotenv_values

# Get the Config from the .env file
basedir = os.path.abspath(os.path.dirname(__file__))
CONFIG = dotenv_values(os.path.join(basedir, "instance", ".env"))

"""
? SECRET_KEY: 
Key used to secure the sessions that remember information from one request to another. 
User can access the information stored in the session but cannot modify it unless they have the SECRET_KEY 

? SQLALCHEMY_DATABASE_URI: 
The database URI specifies the database you want to establish a connection with using SQLAlchemy

? SQLALCHEMY_TRACK_MODIFICATIONS:  
A configuration to enable or disable tracking modifications of objects.
"""


class Config:
    SECRET_KEY = None
    DATABASE = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATION = False
    USER=None
    PASSWORD=None

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DATABASE = os.path.join(basedir, 'instance', 'library_main.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'library_main.db')
    SQLALCHEMY_TRACK_MODIFICATION = False

    
class TestingConfig(Config):
    SECRET_KEY = 'test'
    DATABASE = os.path.join(basedir, 'instance', 'library_test.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'library_test.db')
    SQLALCHEMY_TRACK_MODIFICATION = False


# Configuration for production code
# Load from .env file
class ProductionConfig(Config):
    SECRET_KEY = CONFIG["SECRET_KEY"]
    DATABASE = CONFIG["DATABASE"]
    SQLALCHEMY_DATABASE_URI = CONFIG["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATION = bool(CONFIG["SQLALCHEMY_TRACK_MODIFICATION"])
    
    MAIL_SERVER = CONFIG['MAIL_SERVER']
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = CONFIG['MAIL_USERNAME']
    MAIL_PASSWORD = CONFIG['MAIL_PASSWORD']
    MAIL_DEFAULT_SENDER = CONFIG['MAIL_DEFAULT_SENDER']
    
# Configuration by name
config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'product': ProductionConfig
}