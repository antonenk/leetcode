#!/usr/bin/python3

# https://leetcode.com/problems/koko-eating-bananas/description/
# beats 87% runtime / 50% mem

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        minK = 0
        maxK = max(piles)
        while maxK - minK > 1:
            newK = (minK + maxK) // 2
            hoursToEat = sum([math.ceil(pile / newK) for pile in piles])
            if hoursToEat > h:
                minK = newK
            else:
                maxK = newK
        return maxK


def test_1():
    assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4


def test_2():
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30


def test_3():
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23


def test_4():
    assert Solution().minEatingSpeed([312884470], 968709470) == 1


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
