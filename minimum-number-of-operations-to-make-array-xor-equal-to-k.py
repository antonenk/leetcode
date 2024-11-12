#!/usr/bin/python3

# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/
# beats 9% runtime / 20% mem


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        xor_result = k
        for num in nums:
            xor_result = xor_result ^ num
        return bin(xor_result).count("1")


def test_1():
    assert Solution().minOperations([2, 1, 3, 4], 1) == 2


def test_2():
    assert Solution().minOperations([2, 0, 2, 0], 0) == 0


if __name__ == '__main__':
    test_1()
    test_2()
