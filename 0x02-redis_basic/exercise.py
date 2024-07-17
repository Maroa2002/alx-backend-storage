#!/usr/bin/env python3
""" Demonstrating simple cache using redis """

import redis
import uuid
from typing import Union


class Cache:
    """
    A simple cache class using redis
    """
    def __init__(self):
        """
        Initialize the cache with a connection to Redis and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in the cache with a random UUID as the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The UUID key as a string.
        """
        random_uuid = str(uuid.uuid4())  # convert to string
        self._redis.set(random_uuid, data)
        return random_uuid  # returns the UUID key as a string
