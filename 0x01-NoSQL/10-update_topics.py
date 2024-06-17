#!/usr/bin/env python3
""" Change school topics """


def update_topics(mongo_collection, name, topics):
    """
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) will be list of topics approached in the school
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
