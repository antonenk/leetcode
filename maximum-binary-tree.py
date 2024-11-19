#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 47% runtime / 17% mem

from typing import Optional
from leetcode import TreeNode


def constructBinaryTree(nums: list[int]):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return TreeNode(val=nums[0])
    else:
        indexOfMax = nums.index(max(nums))
        return TreeNode(
            val=nums[indexOfMax],
            left=constructBinaryTree(nums[0:indexOfMax]),
            right=constructBinaryTree(nums[indexOfMax + 1:])
        )


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        return constructBinaryTree(nums)


def test_1():
    Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    assert 1 == 1


def test_2():
    Solution().constructMaximumBinaryTree([3, 2, 1])
    assert 1 == 1


if __name__ == '__main__':
    test_1()
    test_2()
