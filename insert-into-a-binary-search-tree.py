#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 36% runtime / 40% mem

from leetcode import TreeNode
from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> TreeNode:
        if root is None:
            return TreeNode(val=val)
        node = root
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val=val)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val=val)
                    break
                else:
                    node = node.right
        return root


def test_1():
    root = TreeNode(
        val=4,
        left=TreeNode(
            val=2,
            left=TreeNode(val=1),
            right=TreeNode(val=3)
            ),
        right=TreeNode(val=7)
        )
    root = Solution().insertIntoBST(root, 5)
    assert root.right.left.val == 5


def test_4():
    root = Solution().insertIntoBST(None, 5)
    assert root.val == 5


if __name__ == '__main__':
    test_1()
    test_4()
