#!/usr/bin/python3

# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
# beats 100% runtime / 29% mem

from typing import Optional
from leetcode import TreeNode


def walkTree(node: TreeNode, target: int) -> bool:
    if node.left is not None and walkTree(node.left, target):
        node.left = None
    if node.right is not None and walkTree(node.right, target):
        node.right = None
    return node.left is None and node.right is None and node.val == target


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> Optional[TreeNode]:
        if walkTree(root, target):
            return None
        else:
            return root


def test_1():
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=2)
            ),
        right=TreeNode(
            val=3,
            left=TreeNode(val=2),
            right=TreeNode(val=4)
            )
        )
    Solution().removeLeafNodes(root, 2)
    assert root.left is None
    assert root.right.left is None


def test_2():
    root = TreeNode(
        val=1,
        left=TreeNode(val=1),
        right=TreeNode(val=1)
        )
    assert Solution().removeLeafNodes(root, 1) is None


if __name__ == '__main__':
    test_1()
    test_2()
