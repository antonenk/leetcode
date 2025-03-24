#!/usr/bin/python3

# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
# beats 94% runtime / 50% mem


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operationsCount = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                operationsCount += 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return operationsCount


def test_1():
    assert Solution().minOperations([0, 1, 1, 1, 0, 0]) == 3


def test_2():
    assert Solution().minOperations([0, 1, 1, 1]) == -1


if __name__ == '__main__':
    test_1()
    test_2()
