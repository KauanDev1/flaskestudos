from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

#config do sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'AJGSD6912FED1727WX12RW1782RX812T716TV2X'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.views import homepage
from app.models import Contato