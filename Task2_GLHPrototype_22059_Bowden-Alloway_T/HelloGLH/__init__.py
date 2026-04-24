from flask import Flask
app = Flask(__name__)

import HelloGLH.views

app.config['SECRET_KEY'] = 'tobeannounced'