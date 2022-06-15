from flask import Flask
from firebase_admin import credentials,initialize_app

cred=credentials.Certificate("api/key.json")
default_app=initialize_app(cred,{'databaseURL':'https://sensores-diego-esp32-default-rtdb.firebaseio.com/'})

def create_app():
    app=Flask(__name__)

    from .userAPI import userAPI
    app.register_blueprint(userAPI,url_prefix='/data')

    return app