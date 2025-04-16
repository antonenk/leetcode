#!/usr/bin/python3

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# beats 98% runtime / 15% mem

from leetcode import TreeNode


def walkTree(node: TreeNode, maxParent: int) -> int:
    if node.val < maxParent:
        result = 0
    else:
        result = 1
        maxParent = node.val

    if node.left:
        result += walkTree(node.left, maxParent)
    if node.right:
        result += walkTree(node.right, maxParent)

    return result


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return walkTree(root, root.val)


def test_1():
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=1,
            left=TreeNode(val=3)
            ),
        right=TreeNode(
            val=4,
            left=TreeNode(val=1),
            right=TreeNode(val=5)
            )
        )
    assert Solution().goodNodes(root) == 4


if __name__ == '__main__':
    test_1()
