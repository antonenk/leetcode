#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 46% mem


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            s2 = s.replace(part, "", 1)
            if s == s2:
                break
            else:
                s = s2
        return s


def test_1():
    assert Solution().removeOccurrences("daabcbaabcbc", "abc") == "dab"


def test_2():
    assert Solution().removeOccurrences("axxxxyyyyb", "xy") == "ab"


if __name__ == '__main__':
    test_1()
    test_2()
