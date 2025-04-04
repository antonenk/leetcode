#!/usr/bin/python3

# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/
# beats 74% runtime / 15% mem


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        subsetsCount = 1
        subsetMax = nums[0] + k
        for num in nums:
            if num > subsetMax:
                subsetsCount += 1
                subsetMax = num + k
        return subsetsCount


def test_1():
    assert Solution().partitionArray([3, 6, 1, 2, 5], 2) == 2


def test_2():
    assert Solution().partitionArray([1, 2, 3], 1) == 2


def test_3():
    assert Solution().partitionArray([2, 2, 4, 5], 0) == 3


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
