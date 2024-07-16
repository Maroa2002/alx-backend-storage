#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """
        inserts a new document in a collection based on kwargs
        args:
            mongo_collection: pymongo collection object
            **kwargs: keywords arguments with attribute values
        return: new _id
    """
    doc = {
            "name": kwargs.get('name'),
            "address": kwargs.get('address')
        }
    res = mongo_collection.insert_one(doc)
    return res.inserted_id
