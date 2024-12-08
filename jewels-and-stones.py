#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 11% mem


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        jewelsCount = 0
        for stone in stones:
            if stone in jewelsSet:
                jewelsCount += 1
        return jewelsCount


def test_1():
    assert Solution().numJewelsInStones("aA", "aAAbbbb") == 3


def test_2():
    assert Solution().numJewelsInStones("z", "ZZ") == 0


if __name__ == '__main__':
    test_1()
    test_2()
