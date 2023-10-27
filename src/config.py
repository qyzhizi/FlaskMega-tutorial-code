import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    EMPLATE_DIR = "/app/src/application/templates"

    # Top secret of website
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'    
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or '*****************'  
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or '*****************' 

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Gmail Config
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = '465'
    MAIL_USE_SSL = True
    # MAIL_DEBUG : default app.debug
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or '*****************'
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or '*****************'