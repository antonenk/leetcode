#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 7% mem

from itertools import chain, combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        for subset in chain.from_iterable(combinations(nums, r) for r in range(0, len(nums)+1)):
            result.append(list(subset))
        return result


def test_1():
    assert Solution().subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]


def test_2():
    assert Solution().subsets([0]) == [[], [0]]


if __name__ == '__main__':
    test_1()
    test_2()
