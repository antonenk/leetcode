#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 63% runtime / 12% mem


class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinctNums = set(nums)
        distinctNums |= set([int(str(num)[::-1]) for num in nums])
        return len(distinctNums)


def test_1():
    assert Solution().countDistinctIntegers([1, 13, 10, 12, 31]) == 6


def test_2():
    assert Solution().countDistinctIntegers([2, 2, 2]) == 1


if __name__ == '__main__':
    test_1()
    test_2()
