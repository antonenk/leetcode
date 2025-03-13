#!/usr/bin/python3

# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
# beats 12% runtime / 85% mem

import itertools


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        patternLength = len(pattern)
        for digits in itertools.permutations(range(1, 10), patternLength + 1):
            isMatched = True
            for i in range(patternLength):
                if digits[i] < digits[i + 1]:
                    if pattern[i] == "D":
                        isMatched = False
                        break
                else:
                    if pattern[i] == "I":
                        isMatched = False
                        break
            if isMatched:
                break
        return "".join([str(d) for d in digits])


def test_1():
    assert Solution().smallestNumber("IIIDIDDD") == "123549876"


def test_2():
    assert Solution().smallestNumber("DDD") == "4321"


if __name__ == '__main__':
    test_1()
    test_2()
