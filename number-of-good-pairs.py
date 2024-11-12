#!/usr/bin/python3

# https://leetcode.com/problems/number-of-good-pairs/description/
# beats 100% runtime / 53% mem

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result = 0
        nums_count = {}
        for num in nums:
            if num in nums_count:
                result += nums_count[num]
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        return result


def test_1():
    assert Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4


def test_2():
    assert Solution().numIdenticalPairs([1, 1, 1, 1]) == 6


def test_3():
    assert Solution().numIdenticalPairs([1, 2, 3]) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
