"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
"""

import string
import random
class Codec:
    def __init__(self):
        self.size = 10000
        self.map = [None]*self.size

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = 'http://tinyurl.com/'.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 7))
        ID = 0
        for i in shortUrl:
            ID += ord(i)
        ID = (ID//100)+1
        if self.map[ID]==None:
            self.map[ID] = [[ID,shortUrl,longUrl]]
            return shortUrl
        for m in self.map[ID]:
            if m[-1]==longUrl: return
        self.map[ID].append([ID,shortUrl,longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        ID = 0
        for i in shortUrl:
            ID += ord(i)
        ID = (ID//100)+1
        if self.map[ID]!=None:
            for m in self.map[ID]:
                if m[1]==shortUrl: return m[-1]
