#!/usr/bin/python3

# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description/
# beats 85% runtime / 56% mem


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(len(s) - s.count('a') * 2)


def test_1():
    assert Solution().minLengthAfterRemovals("aabbab") == 0


def test_2():
    assert Solution().minLengthAfterRemovals("aaaa") == 4


def test_3():
    assert Solution().minLengthAfterRemovals("aaabb") == 1


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
