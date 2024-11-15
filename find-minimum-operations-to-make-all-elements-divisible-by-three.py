#!/usr/bin/python3

# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 != 0:
                operations += 1
        return operations


def test_1():
    assert Solution().minimumOperations([1, 2, 3, 4]) == 3


def test_2():
    assert Solution().minimumOperations([3, 6, 9]) == 0


if __name__ == '__main__':
    test_1()
    test_2()
