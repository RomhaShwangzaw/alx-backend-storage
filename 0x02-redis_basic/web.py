#!/usr/bin/env python3
"""Expiring web cache Module"""
import redis
import requests
from functools import wraps
from typing import Callable


r = redis.Redis()


def count_url(method: Callable) -> Callable:
    """
    A wrapper function that tracks how many times
    a particular URL was accessed. It caches the
    result with an expiration time of 10 seconds.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function that caches the result"""
        r.incr(f"count:{url}")
        result = r.get(f"result:{url}")
        if result:
            return result.decode()
        result = method(url)
        r.set(f"count:{url}", 0)
        r.setex(f"result:{url}", 10, result)
        return result
    return wrapper


@count_url
def get_page(url: str) -> str:
    """
    Uses the `requests` module to obtain the HTML
    content of a particular URL and returns it.
    """
    result = requests.get(url)
    return result.text
