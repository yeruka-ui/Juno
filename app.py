from flask import Flask, render_template
from dotenv import load_dotenv
import os
from routes.api import api_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route('/')
    def home():
        return render_template("login.html")
        
    return app

'''TO RUN APPLICATION (IN TERMINAL): 
.\.venv\Scripts\Activate.ps1 (ACTIVATE ENVIRONMENT)
$env:FLASK_APP = "app:create_app"
$env:FLASK_ENV = "development"
flask run
 '''