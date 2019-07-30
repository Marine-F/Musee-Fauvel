import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'vous_ne_devinerez_jamais'
    # la clé secrète sert de protection contres certains hacks.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "sqlite:///" + os.path.join(basedir, 'BDD_Fauvel.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # chemin vers la base de données sqlite.
