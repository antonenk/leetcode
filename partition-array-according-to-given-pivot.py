#!/usr/bin/python3

# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
# beats 64% runtime / 51% mem
# score: medium

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return less + equal + greater


def test_1():
    assert Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10) == [9, 5, 3, 10, 10, 12, 14]


def test_2():
    assert Solution().pivotArray([-3, 4, 3, 2], 2) == [-3, 2, 4, 3]


if __name__ == '__main__':
    test_1()
    test_2()
