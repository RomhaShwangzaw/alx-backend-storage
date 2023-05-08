#!/usr/bin/env python3
"""List all documents module"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Arg:
        mongo_collection: a pymongo collection object

    Return:
        a list of all documents in the collection, or
        an empty list if no document in the collection
    """
    return list(mongo_collection.find())
