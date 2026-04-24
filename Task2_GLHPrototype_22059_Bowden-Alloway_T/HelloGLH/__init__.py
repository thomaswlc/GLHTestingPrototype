from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "tobeannounced"   # required for sessions

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "signin"  # redirects if not logged in

import HelloGLH.views