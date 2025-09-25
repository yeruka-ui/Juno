from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("main.html") 
        
    return app

'''TO RUN APPLICATION (IN TERMINAL): 
$env:FLASK_APP = "app:create_app"
$env:FLASK_ENV = "development"
flask run
 '''