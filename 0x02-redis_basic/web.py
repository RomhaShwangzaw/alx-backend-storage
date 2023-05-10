#!/usr/bin/env python3
"""Expiring web cache Module"""
import redis
import requests
from functools import wraps


r = redis.Redis()


def count_url(method: Callable) -> Callable:
    """
    A wrapper function that tracks how many times
    a particular URL was accessed. It caches the
    result with an expiration time of 10 seconds.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        r.incr(f"count:{args[0]}")
        r.expire(f"count:{args[0]}", 10)
        return method(*args, **kwargs)
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    Uses the `requests` module to obtain the HTML
    content of a particular URL and returns it.
    """
    result = requests.get(url)
    return result.text
