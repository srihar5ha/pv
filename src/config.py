# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = "development secret key"
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = "prod secret key"

app_config = {
    'development': Development,
    'production': Production,
}