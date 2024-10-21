#!/usr/bin/python3

class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        result = [pref[0]]
        for i in range(1, len(pref)):
            result.append(pref[i-1] ^ pref[i])
        return result


def test_1():
    assert Solution().findArray([5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]


def test_2():
    assert Solution().findArray([13]) == [13]
