#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 12% runtime / 82% mem


class Solution:
    def rearrangeArray2(self, nums: list[int]) -> list[int]:
        positive = filter(lambda n: n > 0, nums)
        negative = filter(lambda n: n < 0, nums)
        result = []
        for i in range(len(nums) // 2):
            result.append(next(positive))
            result.append(next(negative))
        return result

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = filter(lambda n: n > 0, nums)
        negative = filter(lambda n: n < 0, nums)
        return [num for t in zip(positive, negative) for num in t]


def test_1():
    assert Solution().rearrangeArray([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]


def test_2():
    assert Solution().rearrangeArray([-1, 1]) == [1, -1]


if __name__ == '__main__':
    test_1()
    test_2()

