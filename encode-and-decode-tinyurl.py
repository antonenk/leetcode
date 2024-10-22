#!/usr/bin/python3

# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:

    def __init__(self, baseUrl='http://tinyurl.com/'):
        self.baseUrl = baseUrl
        self.urls = []

    def encode(self, longUrl: str) -> str:
        self.urls.append(longUrl)
        return self.baseUrl + str(len(self.urls) - 1)

    def decode(self, shortUrl: str) -> str:
        return self.urls[int(shortUrl[len(self.baseUrl):])]


def test_1():
    codec = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    assert codec.decode(codec.encode(url)) == url


if __name__ == '__main__':
    test_1()
