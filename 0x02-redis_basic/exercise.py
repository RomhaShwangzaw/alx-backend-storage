#!/usr/bin/env python3
"""Writing strings to Redis Module"""
import redis
import uuid
from typing import Union


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
