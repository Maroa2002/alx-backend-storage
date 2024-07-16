#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    args:
        mongo_collection: pymongo collection object
        topic (string): topic searched
    return: list of schools
    """
    return mongo_collection.find({'topics': topic})
