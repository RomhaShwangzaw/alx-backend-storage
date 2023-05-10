#!/usr/bin/env python3
"""Redis Module"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Cache class"""
    def __init__(self):
        """Initializer module"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores the input data in Redis using a randomly
        generated key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Optional[
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
