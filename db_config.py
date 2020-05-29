import os
from dotenv import load_dotenv
load_dotenv()

# we define the connection path with the acceses
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://' + os.getenv('DB_USER') + ':' + os.getenv('DB_PSW') + '@' + os.getenv('DB_URL') + '/' + os.getenv('DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False