#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 98% runtime / 52% mem


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) // 3):
            j = i * 3
            if nums[j + 2] - nums[j] > k:
                return []
            result.append([nums[j], nums[j + 1], nums[j + 2]])
        return result


def test_0():
    nums = [1, 3, 4, 8, 7, 10, 3, 5, 1]
    expected = []
    assert Solution().divideArray(nums, 2) == expected


def test_1():
    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
    assert Solution().divideArray(nums, 2) == expected


if __name__ == '__main__':
    test_0()
    test_1()
