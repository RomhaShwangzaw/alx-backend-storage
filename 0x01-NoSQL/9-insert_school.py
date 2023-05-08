#!/usr/bin/env python3
"""Insert document module"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection

    Args:
        * mongo_collection: a pymongo collection object
        * kwargs: a list of named arguments

    Return:
        the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
