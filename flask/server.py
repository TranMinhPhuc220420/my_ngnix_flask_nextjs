#!/usr/bin/env python
import os

from flask_cors import CORS, cross_origin
from flask import Flask
from pymongo import MongoClient

from blueprints.auth.auth import auth_bp

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static/videos'

# ALL BLUEPRINTS...
app.register_blueprint(auth_bp)

@app.errorhandler(400)
def handle_bad_request(e):
	return 'Bad Request', 400
@app.errorhandler(502)
def handle_bad_gateway(e):
	return 'Bad Gateway', 502
@app.errorhandler(404)
def handle_notfound(e):
	return 'Not Found', 404
@app.errorhandler(500)
def handle_internalservererror(e):
	return 'Internal Server Error', 500

CORS(app, origins=[os.getenv('CORS_ORIGINS')], supports_credentials=True)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("FLASK_HOST", '0.0.0.0'),
        port=os.environ.get("FLASK_SERVER_PORT", 9090),
        debug=os.environ.get("FLASK_DEBUG_MODE", False)
    )
