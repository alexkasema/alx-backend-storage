#!/usr/bin/env python3
""" Nginx Log stats """

from pymongo import MongoClient


def main():
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_log_stats(client.logs.nginx)


def print_nginx_log_stats(nginx_collection):
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        doc_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, doc_count))

    status_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})))

    print('{} status check'.format(status_count))

    ips = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    print("Ips:")
    for result in nginx_collection.aggregate(ips):
        print("\t{}: {}".format(result.get('_id'), result.get('count')))


if __name__ == '__main__':
    main()
