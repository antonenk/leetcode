#!/usr/bin/python3

# https://leetcode.com/problems/vowels-game-in-a-string/description/
# beats 95% runtime / 95% mem

import re


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return not re.search('[aeiou]', s) is None


def test_1():
    assert Solution().doesAliceWin("leetcoder") is True


def test_2():
    assert Solution().doesAliceWin("ltcdr") is False


if __name__ == '__main__':
    test_1()
    test_2()
