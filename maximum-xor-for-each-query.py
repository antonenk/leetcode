#!/usr/bin/python3

# https://leetcode.com/problems/maximum-xor-for-each-query/description/
# beats 94% runtime / 24% mem


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        maximum = 2 ** maximumBit - 1
        results = []
        totalXor = 0
        for num in nums:
            totalXor ^= num
            results.append(maximum ^ totalXor)
        results.reverse()
        return results


def test_1():
    nums = [0, 1, 1, 3]
    maximumBit = 2
    output = Solution().getMaximumXor(nums, maximumBit)
    expected = [0, 3, 2, 3]
    assert output == expected


def test_2():
    nums = [2, 3, 4, 7]
    maximumBit = 3
    output = Solution().getMaximumXor(nums, maximumBit)
    expected = [5, 2, 6, 5]
    assert output == expected


def test_3():
    nums = [0, 1, 2, 2, 5, 7]
    maximumBit = 3
    output = Solution().getMaximumXor(nums, maximumBit)
    expected = [4, 3, 6, 4, 6, 7]
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
