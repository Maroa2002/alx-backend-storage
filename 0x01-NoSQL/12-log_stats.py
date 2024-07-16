#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    # connect to MongoDB server
    client = MongoClient()

    # connect to database and collection
    nginx_collection = client.logs.nginx

    # get total number of logs
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        log_count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, log_count))

    # number of logs with method GET and path /status
    status_check_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    log_stats()
