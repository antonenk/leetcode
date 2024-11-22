#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 29% runtime / 90% mem

from itertools import chain, combinations


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        maximumOr = 0
        for num in nums:
            maximumOr |= num

        goodSubsetsCount = 0
        subsets = chain.from_iterable(combinations(nums, r) for r in range(1, len(nums)+1))
        for subset in subsets:
            subsetOr = 0
            for num in subset:
                subsetOr |= num
            if subsetOr == maximumOr:
                goodSubsetsCount += 1
        return goodSubsetsCount


def test_1():
    assert Solution().countMaxOrSubsets([3, 1]) == 2


def test_2():
    assert Solution().countMaxOrSubsets([2, 2, 2]) == 7


def test_3():
    assert Solution().countMaxOrSubsets([3, 2, 1, 5]) == 6


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
