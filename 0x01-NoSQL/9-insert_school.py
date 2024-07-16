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
    # creating the document directly from kwargs
    doc = kwargs
    # inserting the document into the collection
    res = mongo_collection.insert_one(doc)
    # returning the new _id
    return res.inserted_id
