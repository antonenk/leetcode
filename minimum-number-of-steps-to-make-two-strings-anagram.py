#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 67% runtime / 64% mem

from functools import reduce


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        baseOrd = ord('a')
        letters = [0] * 26
        for c in s:
            letters[ord(c) - baseOrd] += 1
        for c in t:
            letters[ord(c) - baseOrd] -= 1
        diffsCount = reduce(lambda a, b: a + abs(b), letters, 0)
        return diffsCount // 2


def test_1():
    assert Solution().minSteps("bab", "aba") == 1


def test_2():
    assert Solution().minSteps("leetcode", "practice") == 5


if __name__ == '__main__':
    test_1()
    test_2()
