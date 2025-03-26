#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 50% runtime / 55% mem


class Solution:
    def minimumLength(self, s: str) -> int:
        symbolsCount = [0] * (ord("z") + 1)
        for symbol in s:
            code = ord(symbol)
            if symbolsCount[code] == 1:
                symbolsCount[code] = 2
            else:
                symbolsCount[code] = 1
        return sum(symbolsCount)


def test_1():
    assert Solution().minimumLength("abaacbcbb") == 5


def test_2():
    assert Solution().minimumLength("aa") == 2


def test_3():
    assert Solution().minimumLength("qz") == 2


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
