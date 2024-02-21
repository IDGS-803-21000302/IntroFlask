
import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    secret_key='clave_nueva'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://bibliovuelo:admin@127.0.0.1/prueba'

    SQLALCHEMY_TRACK_MODIFICATIONS=False
