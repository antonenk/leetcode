#!/usr/bin/python3

# https://leetcode.com/problems/deepest-leaves-sum/description/
# beats 67% runtime / 23% mem

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def walkTree(node: TreeNode, level=0) -> int:
    deepest_level = level
    sum_on_deepest_level = node.val
    if node.right is not None:
        deepest_level, sum_on_deepest_level = walkTree(node.right, level + 1)
    if node.left is not None:
        another_level, sum_on_another_level = walkTree(node.left, level + 1)
        if another_level > deepest_level:
            deepest_level = another_level
            sum_on_deepest_level = sum_on_another_level
        elif another_level == deepest_level:
            sum_on_deepest_level += sum_on_another_level
    return deepest_level, sum_on_deepest_level


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_level, sum_on_deepest_level = walkTree(root, 0)
        return sum_on_deepest_level


def test_1():
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(
                val=4,
                left=TreeNode(val=7)
                ),
            right=TreeNode(val=5),
            ),
        right=TreeNode(
            val=3,
            right=TreeNode(
                val=6,
                right=TreeNode(val=8)
                )
            )
        )
    assert Solution().deepestLeavesSum(root) == 15


def test_2():
    root = TreeNode(
        val=6,
        left=TreeNode(
            val=7,
            left=TreeNode(
                val=2,
                left=TreeNode(val=9)
                ),
            right=TreeNode(
                val=7,
                left=TreeNode(val=1),
                right=TreeNode(val=4)
                )
            ),
        right=TreeNode(
            val=8,
            left=TreeNode(val=1),
            right=TreeNode(
                val=3,
                right=TreeNode(val=5)
                )
            )
        )
    assert Solution().deepestLeavesSum(root) == 19


def test_my1():
    root = TreeNode(
        val=6,
        left=TreeNode(
            val=7,
            left=TreeNode(
                val=2,
                left=TreeNode(val=9)
                ),
            right=TreeNode(
                val=7,
                left=TreeNode(val=1),
                right=TreeNode(val=4)
                )
            ),
        right=TreeNode(
            val=8,
            left=TreeNode(val=1),
            right=TreeNode(
                val=3,
                right=TreeNode(val=5)
                )
            )
        )
    assert Solution().deepestLeavesSum(root) == 19


def test_my2():
    root = TreeNode(val=42)
    assert Solution().deepestLeavesSum(root) == 42


if __name__ == '__main__':
    test_1()
    test_2()
    test_my1()
    test_my2()
