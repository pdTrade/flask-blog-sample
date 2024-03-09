import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'my precious'
USERNAME = 'admin'
PASSWORD = 'pass'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
