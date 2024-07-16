#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    args:
        mongo_collection: pymongo collection object
        name (string): school name to update
        topics (list of strings): list of topics approached in the school
    """
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
            )
