#!/usr/bin/python3

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
# beats 100% runtime / 32% mem


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        operationsCount = 0
        level = 0
        for ch in s:
            if ch == "(":
                level += 1
            else:
                if level > 0:
                    level -= 1
                else:
                    operationsCount += 1
        operationsCount += level
        return operationsCount


def test_1():
    assert Solution().minAddToMakeValid("())") == 1


def test_2():
    assert Solution().minAddToMakeValid("(((") == 3


if __name__ == '__main__':
    test_1()
    test_2()
