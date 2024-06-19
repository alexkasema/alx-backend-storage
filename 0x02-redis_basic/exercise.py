#!/usr/bin/env python3
""" Writing strings to Redis """

import redis
import uuid
from typing import Union


class Cache:
    """ Stores data in the redis database """
    def __init__(self) -> None:
        """ Initialize the redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the data in redis using a randomly generated key.
        Args:
            data: The data to be stored in Redis
        Returns:
            The generated key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
