#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """ returns a list of all documents in the collection """
    return [doc for doc in mongo_collection.find()]
