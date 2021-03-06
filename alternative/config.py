from os import urandom

class Config(object):
    SECRET_KEY = urandom(24)
    DEBUG = True
    UPLOADED_IMAGES_DEST = 'application/static/images'
    ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jfif'}
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Gratisek123@localhost/bachelor2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False