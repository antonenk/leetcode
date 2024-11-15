#!/usr/bin/python3

# https://leetcode.com/problems/concatenation-of-array/description/


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums


def test_1():
    assert Solution().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]


def test_2():
    assert Solution().getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]


if __name__ == '__main__':
    test_1()
    test_2()
