#!/usr/bin/python3

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        nums_count = [0] * (len(nums) + 1)
        rows = 1
        for num in nums:
            nums_count[num] += 1
            if rows < nums_count[num]:
                rows = nums_count[num]

        result = []
        for row in range(rows):
            result.append([])

        for num in range(len(nums_count)):
            for row in range(nums_count[num]):
                result[row].append(num)

        return result


def test_1():
    assert Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]) == [[1, 2, 3, 4], [1, 3], [1]]


def test_2():
    assert Solution().findMatrix([1, 2, 3, 4]) == [[1, 2, 3, 4]]


if __name__ == '__main__':
    test_1()
    test_2()
