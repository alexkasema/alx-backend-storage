#!/usr/bin/env python3
""" Writing strings to Redis """

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """
        Retrieves data from Redis and optionally apply a conversion function
        Args:
            key: The key to retrieve the data.
            fn: a function to convert the data to desired format.
        Returns:
            The data from Redis, possibly converted the format by fn, or None
            if key does not exist
        """
        data = self._redis.get(key)

        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string from Redis
        Args:
            keys: The key to retrieve data
        Returns:
        The data as a string or None if key does not exist.
        """
        data = self.get(key, fn=lambda value: value.decode('utf-8'))
        return data

    def get_int(self, key: str) -> int:
        """
        Retrieve an Integer from Redis
        Args:
            keys: The key to retrieve data
        Returns:
            The data as integer, or None if key does not exist
        """
        return self.get(key, fn=lambda value: int(value))
