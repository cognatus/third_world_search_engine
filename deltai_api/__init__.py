# In this file we call all the imports of the project and also start it

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db_config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from deltai_api import routes, models
