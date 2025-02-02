#!/usr/bin/python3

# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
# beats 63% runtime / 11% mem

from typing import Tuple
from leetcode import TreeNode


def walkTree(node: TreeNode) -> Tuple[int, int, int]:
    node_val = node.val
    if node.left:
        left_min_val, left_max_val, left_max_diff = walkTree(node.left)
    else:
        left_min_val = node_val
        left_max_val = node_val
        left_max_diff = 0

    if node.right:
        right_min_val, right_max_val, right_max_diff = walkTree(node.right)
    else:
        right_min_val = node_val
        right_max_val = node_val
        right_max_diff = 0

    min_val = min(left_min_val, right_min_val, node_val)
    max_val = max(left_max_val, right_max_val, node_val)
    max_diff = max(left_max_diff, right_max_diff, abs(max_val - node_val), abs(node_val - min_val))
    return min_val, max_val, max_diff


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        min_val, max_val, max_diff = walkTree(root)
        return max_diff


def test_1():
    root = TreeNode(
        val=8,
        left=TreeNode(
            val=3,
            left=TreeNode(val=1),
            right=TreeNode(
                val=6,
                left=TreeNode(val=4),
                right=TreeNode(val=7)
                )
            ),
        right=TreeNode(
            val=10,
            right=TreeNode(
                val=14,
                left=TreeNode(val=13)
                )
            )
        )
    assert Solution().maxAncestorDiff(root) == 7


def test_2():
    root = TreeNode(
        val=1,
        right=TreeNode(
            val=2,
            right=TreeNode(
                val=0,
                left=TreeNode(val=3)
                )
            )
        )
    assert Solution().maxAncestorDiff(root) == 3


if __name__ == '__main__':
    test_1()
    test_2()
