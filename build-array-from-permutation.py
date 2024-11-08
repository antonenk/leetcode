#!/usr/bin/python3

# https://leetcode.com/problems/build-array-from-permutation/description/


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[num] for num in nums]


def test_1():
    assert Solution().buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]


def test_2():
    assert Solution().buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]


if __name__ == '__main__':
    test_1()
    test_2()
