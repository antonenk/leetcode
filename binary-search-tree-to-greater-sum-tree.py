#!/usr/bin/python3

# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
# beats 100% runtime / 36% mem


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addGreaterValuesToNodes(node: TreeNode, sumGreaterNodes):
    if node.right is not None:
        sumGreaterNodes = addGreaterValuesToNodes(node.right, sumGreaterNodes)
    # print(node.val, "->")
    node.val += sumGreaterNodes
    # print("->", node.val)
    sumGreaterNodes = node.val
    if node.left is not None:
        sumGreaterNodes = addGreaterValuesToNodes(node.left, sumGreaterNodes)
    return sumGreaterNodes


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        addGreaterValuesToNodes(root, 0)
        return root


def test_1():
    root = TreeNode(
        val=4,
        left=TreeNode(
            val=1,
            left=TreeNode(val=0),
            right=TreeNode(
                val=2,
                right=TreeNode(val=3)
                )
            ),
        right=TreeNode(
            val=6,
            left=TreeNode(val=5),
            right=TreeNode(
                val=7,
                right=TreeNode(val=8)
                )
            )
        )
    Solution().bstToGst(root)
    assert 1 == 1


if __name__ == '__main__':
    test_1()
