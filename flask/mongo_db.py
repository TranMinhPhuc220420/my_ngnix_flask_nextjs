import logging
import os
from bson import ObjectId

from plt_utils import JSONEncoder

from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_DB_CONNECT'))
db = client.flask_database


class UsersCollection:
  collections = db.users
  fields = [
    {'name': '_id', 'type_of': ObjectId, 'required': True},
    {'name': 'username', 'type_of': str, 'required': True},
    {'name': 'password_hash', 'type_of': str, 'required': True},
    {'name': 'avatar_url', 'type_of': str, 'required': True},
  ]

  def __init__(self):
    logging.info('_Init UsersCollection class')

  # ===================================================================
  # Define setter
  # ===================================================================

  @classmethod
  def insert(cls, params):

    for item in cls.fields:
      is_required_field = item.get('required')
      name_field = item.get('name')
      type_of_field = item.get('type_of')

      value_in_params = params.get(name_field)
      if is_required_field and value_in_params is None and isinstance(value_in_params, type_of_field):
        return False, 'required'

    cls.collections.insert_one(params)

    return None

  # ===================================================================
  # Define getter dict
  # ===================================================================

  @classmethod
  def get_dict(cls, _id):
    doc = cls.collections.find_one({"_id": ObjectId(_id)})

    if doc:
      return JSONEncoder().encode(doc)

    return None

  @classmethod
  def get_dict_by_username(cls, username):
    doc = cls.collections.find_one({"username": username})

    if doc:
      return JSONEncoder().encode(doc)

    return None
