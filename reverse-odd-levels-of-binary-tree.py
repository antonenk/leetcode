#!/usr/bin/python3

# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
# beats 86% runtime / 80% mem

from typing import Optional
from leetcode import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [root]
        isOddLevel = False
        while level[0].left is not None:
            newLevel = []
            isOddLevel = not isOddLevel
            for node in level:
                newLevel.append(node.left)
                newLevel.append(node.right)
            level = newLevel
            if isOddLevel:
                for i in range((len(level) + 1) // 2):
                    leftValue = level[i].val
                    level[i].val = level[-1 - i].val
                    level[-1 - i].val = leftValue
        return root


def test_1():
    root = TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=TreeNode(val=8),
            right=TreeNode(val=13)
            ),
        right=TreeNode(
            val=5,
            left=TreeNode(val=21),
            right=TreeNode(val=34)
            )
        )
    Solution().reverseOddLevels(root)
    assert root.left.val == 5
    assert root.right.val == 3


def test_2():
    root = TreeNode(
        val=7,
        left=TreeNode(val=13),
        right=TreeNode(val=11)
        )
    Solution().reverseOddLevels(root)
    assert root.left.val == 11
    assert root.right.val == 13


if __name__ == '__main__':
    test_1()
    test_2()
