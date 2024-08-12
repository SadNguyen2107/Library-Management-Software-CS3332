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
CONFIG = dotenv_values(os.path.join(basedir, "instance" ,".env"))

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
    SECRET_KEY = CONFIG["SECRET_KEY"] or "dev"
    DATABASE = CONFIG["DATABASE"]
    SQLALCHEMY_DATABASE_URI = (
        CONFIG["SQLALCHEMY_DATABASE_URI"] or "sqlite:///app.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATION = bool(CONFIG["SQLALCHEMY_TRACK_MODIFICATION"]) or False
