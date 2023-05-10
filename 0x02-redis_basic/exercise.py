#!/usr/bin/env python3
"""Redis Module"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A wrapper function that counts how many times the
    wrapped function has been called
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        args[0]._redis.incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A wrapper function that stores the history of inputs
    and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        args[0]._redis.rpush("{}:inputs".
                             format(method.__qualname__), str(args))
        output = method(*args, **kwargs)
        args[0]._redis.rpush("{}:outputs".
                             format(method.__qualname__), str(output))
        return output
    return wrapper


def replay(method: Callable):
    """Displays the history of calls of a particular function."""
    r = redis.Redis()
    name = method.__qualname__
    count = r.get(name)
    print(f"{name} was called {count.decode()} times")
    inputs = r.lrange("{}:inputs".format(name), 0, -1)
    outputs = r.lrange("{}:outputs".format(name), 0, -1)
    zips = zip(inputs, outputs)
    for z in zips:
        print("{}(*{}) -> {}".format(name, z[0].decode(), z[1].decode()))


class Cache:
    """Cache class"""
    def __init__(self):
        """Initializer module"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores the input data in Redis using a randomly
        generated key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[
            Union[str, bytes, int, float]]:
        """
        Retrieves a value from Redis based on the key,
        then converts the value to a desired format
        using the callable function `fn`.

        Return:
            the converted value
        """
        value = self._redis.get(key)
        if not fn or not value:
            return value
        return fn(value)

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a value from Redis based on the key,
        then converts the value to a string.

        Return:
            the converted string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves a value from Redis based on the key,
        then converts the value to an integer.

        Return:
            the converted integer
        """
        return self.get(key, int)
