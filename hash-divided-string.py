#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 65% runtime / 52% mem


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        baseOrd = ord('a')
        hashString = ""
        for substringId in range(len(s) // k):
            hash = 0
            for charId in range(k):
                hash += ord(s[substringId * k + charId]) - baseOrd
            hashString += chr(hash % 26 + baseOrd)

        return hashString


def test_1():
    assert Solution().stringHash("abcd", 2) == "bf"


def test_2():
    assert Solution().stringHash("mxz", 3) == "i"


if __name__ == '__main__':
    test_1()
    test_2()
