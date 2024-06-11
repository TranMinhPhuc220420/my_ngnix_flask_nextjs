import hashlib

from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from flask import send_from_directory

import plt_func
from mongo_db import db, UsersCollection

from plt_utils import JSONEncoder

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

accidents_collection = db.accidents


@auth_bp.route('/uploads/<name>', endpoint='download_file')
def download_file(name):
  return send_from_directory('storages/avatars', name)


# Route for the user to login...
# @auth_bp.route('/login', methods=['POST', 'OPTIONS'])
# @cross_origin(supports_credentials=True)
# def login():
#     login_details = request.get_json()
#     user_from_db = users_collection.find_one({'username': login_details['username']})
#     if user_from_db:
#         print("🔥")
#         encrypted_password = hashlib.sha256(login_details['password'].encode('utf-8')).hexdigest()
#         if encrypted_password == user_from_db['password']:
#             access_token = create_access_token(identity=user_from_db['username'])
#             return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({'msg': "User doesnot exits"}), 404
#     return jsonify({'msg': 'The username or password is incorrect'}), 401


# Route for the user to register...
@auth_bp.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def register():
  username = request.form.get('username')
  password = request.form.get('password')
  avatar_f = request.files['avatar_f']
  password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  doc = users_collection.find_one({"username": username})
  if not doc:
    avatar_url = '/storage/avatar-default.png'
    users_collection.insert_one({
      'username': username,
      'password': password,
      'avatar_url': avatar_url,
    })

    if avatar_f and plt_func.allowed_file(avatar_f.filename):
      entry = users_collection.find_one({'username': username})
      #
      # filename = secure_filename(str(entry.get('_id')) + plt_func.get_dot_file(avatar_f.filename))
      # avatar_f.save(os.path.join('storages/avatars', filename))
      # avatar_url = url_for('auth.download_file', name=filename)
      # users_collection.update_one({'_id': entry.inserted_id}, {'$set': {'avatar_url': avatar_url}})

    return jsonify({'msg': entry}), 201
  else:
    return jsonify({'msg': 'User already exists'}), 409


# Route for the user to get info1...
@auth_bp.route('/info', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def info():
  username = request.form.get('username')

  doc_dict = UsersCollection.get_dict_by_username(username)

  if doc_dict:
    return doc_dict, 201
  else:
    return jsonify({'msg': 'User not already exists'}), 404
