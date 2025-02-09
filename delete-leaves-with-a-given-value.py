#!/usr/bin/python3

# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
# beats 100% runtime / 47% mem

from typing import Optional
from leetcode import TreeNode


def walkTree(node: TreeNode, target: int) -> Optional[TreeNode]:
    if node.left is not None:
        node.left = walkTree(node.left, target)
    if node.right is not None:
        node.right = walkTree(node.right, target)
    if node.left is None and node.right is None and node.val == target:
        return None
    return node


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> Optional[TreeNode]:
        return walkTree(root, target)


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
