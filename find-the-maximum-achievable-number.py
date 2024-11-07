#!/usr/bin/python3

# https://leetcode.com/problems/score-of-a-string/description/


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


def test_1():
    assert Solution().theMaximumAchievableX(4, 1) == 6


def test_2():
    assert Solution().theMaximumAchievableX(3, 2) == 7


if __name__ == '__main__':
    test_1()
    test_2()
