#!/usr/bin/python3

# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
# beats 15% runtime / 40% mem

import itertools


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        patternLength = len(pattern)
        if pattern[0] == "I":
            prefixLength = patternLength + 1
            for i in range(1, patternLength):
                if pattern[i] == "D":
                    prefixLength = i
                    break
            prefix = list(range(1, prefixLength + 1))
        else:
            prefixLength = patternLength + 1
            for i in range(1, patternLength):
                if pattern[i] == "I":
                    prefixLength = i + 1
                    break
            prefix = list(range(prefixLength, 0, -1))

        suffixLength = patternLength + 1 - prefixLength
        if suffixLength == 0:
            return "".join([str(d) for d in prefix])

        suffixDigits = range(prefixLength + 1, 10)
        for suffix in itertools.permutations(suffixDigits, suffixLength):
            isMatched = True
            for i in range(suffixLength - 1):
                if suffix[i] < suffix[i + 1]:
                    if pattern[prefixLength + i] == "D":
                        isMatched = False
                        break
                else:
                    if pattern[prefixLength + i] == "I":
                        isMatched = False
                        break
            if isMatched:
                break

        digits = prefix + list(suffix)
        return "".join([str(d) for d in digits])

    def smallestNumberSimple(self, pattern: str) -> str:
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
