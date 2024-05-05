import os

from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_DB_CONNECT'))
db = client.flask_database