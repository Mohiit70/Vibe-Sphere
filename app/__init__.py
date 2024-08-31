from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['WEATHER_API_KEY'] = os.getenv('WEATHER_API_KEY')

    from app import routes
    
    return app