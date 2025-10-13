from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, auth
from routes.api import api_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")  # Needed for sessions

    # Initialize Firebase Admin
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route('/')
    def login_page():
        return render_template("login.html")

    @app.route('/main')
    def home():
        return render_template("main.html")

    # Route to verify Firebase token from frontend
    @app.route('/login', methods=['POST'])
    def firebase_login():
        data = request.json
        token = data.get("token")
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
            email = decoded_token.get("email")
            # Store in session if you want
            session["uid"] = uid
            session["email"] = email
            return jsonify({"status": "success", "uid": uid, "email": email})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 400

    return app

'''TO RUN APPLICATION (IN TERMINAL): 
//install dependencies
pip install -r requirements.txt
npm install
pip install google-search-results
pip install pywhatkit


//run the app
.venv\Scripts\Activate.ps1
$env:FLASK_APP = "app:create_app"
$env:FLASK_ENV = "development"
flask run
 '''