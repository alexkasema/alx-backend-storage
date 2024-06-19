#!/usr/bin/env python3
""" Writing strings to Redis """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called
    Args:
        method: The method to be decorated.
    Returns:
        A decorated method that increments a counter each time it is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Icrement the counter for the method """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method.
    Args:
        method: The method to be decorated.
    Returns:
        A decorated method that logs its input parameters and output to Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ logs input and output to Redis """
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)

        return output

    return wrapper


class Cache:
    """ Stores data in the redis database """
    def __init__(self) -> None:
        """ Initialize the redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
