#!/usr/bin/python3

# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/
# beats 86% runtime / 100% mem


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            for i in range(1, len(s) - 1):
                if s[i - 1] > s[i] and s[i + 1] > s[i]:
                    waviness += 1
                if s[i - 1] < s[i] and s[i + 1] < s[i]:
                    waviness += 1
        return waviness


def test_1():
    assert Solution().totalWaviness(120, 130) == 3


def test_2():
    assert Solution().totalWaviness(198, 202) == 3


def test_3():
    assert Solution().totalWaviness(4848, 4848) == 2


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
