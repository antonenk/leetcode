#!/usr/bin/python3

# https://leetcode.com/problems/optimal-partition-of-string/description/
# beats 46% runtime / 37% mem


class Solution:
    def partitionString(self, s: str) -> int:
        substringCount = 1
        letterBase = ord('a')
        isLetterInSubstring = [False] * 28
        for letter in s:
            letterCode = ord(letter) - letterBase
            if isLetterInSubstring[letterCode]:
                substringCount += 1
                isLetterInSubstring = [False] * 28
            isLetterInSubstring[letterCode] = True
        return substringCount


def test_1():
    assert Solution().partitionString("abacaba") == 4


def test_2():
    assert Solution().partitionString("ssssss") == 6


def test_3():
    assert Solution().partitionString("azzzaa") == 4


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
