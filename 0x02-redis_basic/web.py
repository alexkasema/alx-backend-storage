#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """

import redis
import requests
from functools import wraps
from typing import Callable


client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the numer of times a method is called
    with a particular url
    Args:
        method: The method to be decorated
    Returns:
        A decorated method that increments a counter for the url
        each time it is called.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        """ increment counter for the url """
        client.incr("count:{}".format(url))

        """ call the original method """
        result = method(url, *args, **kwargs)

        client.set("count:{}".format(url), 0)

        return result

    return wrapper


def cache_result(method: Callable) -> Callable:
    """
    Decorator that caches the results of a method call with a given url
    for 10 seconds.
    Args:
        method: The method to be decorated
    Returns:
        A decorated method that caches the result in Redis
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        """ Caches the result for 10 seconds """
        cached_result = client.get("cache:{}".format(url))
        if cached_result:
            return cached_result.decode("utf-8")

        """ call the original method """
        result = method(url, *args, **kwargs)

        """ cache the result in Redis with an expiration time of 10 seconds"""
        client.setex("cache:{}".format(url), 10, result)

        return result

    return wrapper


@count_calls
@cache_result
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL.
    Args:
        url: The URL to fetch
    Returns:
        The HTML content of the URL as a string.
    """

    response = requests.get(url)

    return response.text
