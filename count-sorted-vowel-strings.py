#!/usr/bin/python3

# https://leetcode.com/problems/count-sorted-vowel-strings/description/
# beats 100% runtime / 34% mem


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dist = [1, 1, 1, 1, 1]
        for i in range(1, n):
            newDist = [0, 0, 0, 0, 0]
            for j in range(5):
                for k in range(j, 5):
                    newDist[k] += dist[j]
            dist = newDist
        return sum(dist)


def test_1():
    assert Solution().countVowelStrings(1) == 5


def test_2():
    assert Solution().countVowelStrings(2) == 15


def test_3():
    assert Solution().countVowelStrings(33) == 66045


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
