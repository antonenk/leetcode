#!/usr/bin/python3

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/
# beats 99% runtime / 88% mem


class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return max([nums[i] + nums[-1 - i] for i in range(len(nums) // 2)])


def test_1():
    assert Solution().minPairSum([3, 5, 2, 3]) == 7


def test_2():
    assert Solution().minPairSum([3, 5, 4, 2, 4, 6]) == 8


if __name__ == '__main__':
    test_1()
    test_2()
