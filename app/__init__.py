"""Here Blueprint is reqistered"""

from flask import Flask

from app.config import app_config

from app.api.codezy import stack


def creatapp():
    myapp = Flask(__name__)
    return myapp


app = creatapp()
app.config.from_object(app_config["development"])
app.register_blueprint(stack)
