#!/usr/bin/python3

# https://leetcode.com/problems/minimum-suffix-flips/description/
# beats 68% runtime / 57% mem


class Solution:
    def minFlips(self, target: str) -> int:
        flipsCount = 0
        previousBit = "0"
        for bit in target:
            if bit != previousBit:
                flipsCount += 1
                previousBit = bit
        return flipsCount


def test_1():
    assert Solution().minFlips("10111") == 3


def test_2():
    assert Solution().minFlips("101") == 3


def test_3():
    assert Solution().minFlips("00000") == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
