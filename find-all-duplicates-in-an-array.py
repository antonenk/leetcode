#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 49% runtime / 32% mem


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        for num in nums:
            positiveNum = abs(num)
            index = positiveNum - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                duplicates.append(positiveNum)

        return duplicates


def test_1():
    assert Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_2():
    assert Solution().findDuplicates([1, 1, 2]) == [1]


def test_3():
    assert Solution().findDuplicates([1]) == []


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
