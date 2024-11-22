#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 47% runtime / 86% mem


from typing import Optional
from leetcode import TreeNode


def getNodesList(root: TreeNode) -> list[TreeNode]:
    if root is None:
        return []
    return getNodesList(root.left) + [root] + getNodesList(root.right)


def buildTreeFromList(nodes: list[TreeNode]) -> TreeNode:
    if len(nodes) == 0:
        return None
    middleIndex = len(nodes) // 2
    root = nodes[middleIndex]
    root.left = buildTreeFromList(nodes[0:middleIndex])
    root.right = buildTreeFromList(nodes[middleIndex + 1:])
    return root


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = getNodesList(root)
        return buildTreeFromList(l)


def test_1():
    root = TreeNode(
        val=1,
        right=TreeNode(
            val=2,
            right=TreeNode(
                val=3,
                right=TreeNode(val=4)
                )
            )
        )
    output = Solution().balanceBST(root)
    expected = output
    assert output == expected


def test_2():
    root = TreeNode(
        val=2,
        left=TreeNode(val=1),
        right=TreeNode(val=3)
        )
    output = Solution().balanceBST(root)
    expected = output
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
