#!/usr/bin/python3

# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/
# beats 74% runtime / 58% mem


class Solution:
    def minChanges(self, s: str) -> int:
        changesNeeded = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changesNeeded += 1
        return changesNeeded


def test_1():
    assert Solution().minChanges("1001") == 2


def test_2():
    assert Solution().minChanges("10") == 1


def test_3():
    assert Solution().minChanges("0000") == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
