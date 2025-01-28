#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 92% runtime / 25% mem

from math import comb


class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            total += comb(n-1, i) * nums[i]
        return total % 10


def test_1():
    assert Solution().triangularSum([1, 2, 3, 4, 5]) == 8


def test_2():
    assert Solution().triangularSum([5]) == 5


def test_3():
    assert Solution().triangularSum([4, 5]) == 9


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
