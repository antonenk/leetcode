#!/usr/bin/python3

# https://leetcode.com/problems/permutations/description/
# beats 100% runtime / 6% mem

from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(p) for p in permutations(nums)]


def test_1():
    assert Solution().permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def test_2():
    assert Solution().permute([0, 1]) == [[0, 1], [1, 0]]


def test_3():
    assert Solution().permute([1]) == [[1]]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
