# manage.py
from flask_migrate import Migrate, MigrateCommand
from databases.ext import db
from flask_script import Manager
from flask import Flask
from config.db import DB_URI
from models.sharefile import ShareFile
from models.shareuser import ShareUser
from models.spiderlist import SpiderList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
