#!/usr/bin/env python3
"""Update document module"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        * mongo_collection: a pymongo collection object
        * name: the school name to update
        * topics: the list of topics approached in the school
    """
    mongo_collection.update_one(
            {'name': name},
            {'$set': {'topics': topics}})
