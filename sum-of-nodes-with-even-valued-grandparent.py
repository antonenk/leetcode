#!/usr/bin/python3

# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
# beats 18% runtime / 36% mem

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def walkTree(node: TreeNode, isParentEven: bool, isGrandParentEven: bool):
    result = 0
    if isGrandParentEven:
        result += node.val
    isEven = node.val % 2 == 0
    if node.right is not None:
        result += walkTree(node.right, isEven, isParentEven)
    if node.left is not None:
        result += walkTree(node.left, isEven, isParentEven)
    return result


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return walkTree(root, False, False)


def test_1():
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
    assert Solution().sumEvenGrandparent(root) == 18


def test_2():
    root = TreeNode(val=1)
    assert Solution().sumEvenGrandparent(root) == 0


if __name__ == '__main__':
    test_1()
    test_2()
