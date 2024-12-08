#!/usr/bin/python3

# https://leetcode.com/problems/maximum-xor-after-operations/description/
# beats 18% runtime / 24% mem


class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        maximumXOR = 0
        for num in nums:
            maximumXOR |= num
        return maximumXOR


def test_1():
    assert Solution().maximumXOR([3, 2, 4, 6]) == 7


def test_2():
    assert Solution().maximumXOR([1, 2, 3, 9, 2]) == 11


if __name__ == '__main__':
    test_1()
    test_2()
