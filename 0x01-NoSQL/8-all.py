#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """
        lists all documents in a collection
        args:
            mongo_collection: pymongo collection object
        return: all documents or empty list if no document
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
