#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 73% mem

from leetcode import TreeNode


def walkTree(node: TreeNode, value: int) -> int:
    if node.left is not None:
        value = walkTree(node.left, value)

    if value < -1:
        value += 1
    elif value == -1:
        return node.val
    else:
        return value

    if node.right is not None:
        value = walkTree(node.right, value)

    return value


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return walkTree(root, -k)


def test_1():
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=1,
            right=TreeNode(val=2)
            ),
        right=TreeNode(4)
        )
    assert Solution().kthSmallest(root, 1) == 1


def test_2():
    root = TreeNode(
        val=5,
        left=TreeNode(
            val=3,
            left=TreeNode(
                val=2,
                left=TreeNode(val=1)
            ),
            right=TreeNode(val=4)
            ),
        right=TreeNode(6)
        )
    assert Solution().kthSmallest(root, 3) == 3


if __name__ == '__main__':
    test_1()
    test_2()
