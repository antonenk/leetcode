#!/usr/bin/python3

# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_indexes = {}
        for i in range(len(nums)):
            nums_indexes[nums[i]] = i

        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in nums_indexes and nums_indexes[second_num] != i:
                return [i, nums_indexes[second_num]]

        return None


def test_1():
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1]


def test_2():
    nums = [3, 2, 4]
    target = 6
    assert Solution().twoSum(nums, target) == [1, 2]


def test_3():
    nums = [3, 3]
    target = 6
    assert Solution().twoSum(nums, target) == [0, 1]


def test_my1():
    nums = [1, 2, 3]
    target = 3
    assert Solution().twoSum(nums, target) == [0, 1]


def test_my2():
    nums = [1, 2, 3]
    target = 5
    assert Solution().twoSum(nums, target) == [1, 2]


def test_my3():
    nums = [1, 2, 3]
    target = 6
    assert Solution().twoSum(nums, target) is None


def test_my4():
    nums = [1, 2, 3]
    target = 7
    assert Solution().twoSum(nums, target) is None


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_my1()
    test_my2()
    test_my3()
    test_my4()
