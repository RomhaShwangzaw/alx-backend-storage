#!/usr/bin/env python3
"""Query with filter module"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic

    Args:
        * mongo_collection: a pymongo collection object
        * topic: the topic searched
    """
    result = mongo_collection.find({'topics': topic})
    return list(result)
