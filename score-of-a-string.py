#!/usr/bin/python3

# https://leetcode.com/problems/score-of-a-string/description/


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i - 1]) - ord(s[i]))
        return score


def test_1():
    assert Solution().scoreOfString('hello') == 13


def test_2():
    assert Solution().scoreOfString('zaz') == 50


if __name__ == '__main__':
    test_1()
    test_2()
