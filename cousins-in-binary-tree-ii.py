#!/usr/bin/python3

# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
# beats 97% runtime / 97% mem

from leetcode import TreeNode


class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        root.val = 0
        thisLevel = [root]
        while len(thisLevel) > 0:
            nextLevel = []
            nextLevelSum = 0
            for node in thisLevel:
                if node.left is not None:
                    nextLevel.append(node.left)
                    nextLevelSum += node.left.val
                if node.right is not None:
                    nextLevel.append(node.right)
                    nextLevelSum += node.right.val

            for node in thisLevel:
                childrenSum = 0
                if node.left is not None:
                    childrenSum += node.left.val
                if node.right is not None:
                    childrenSum += node.right.val

                cousinsSum = nextLevelSum - childrenSum
                if node.left is not None:
                    node.left.val = cousinsSum
                if node.right is not None:
                    node.right.val = cousinsSum
            thisLevel = nextLevel

        return root


def test_1():
    root = TreeNode(
        val=5,
        left=TreeNode(
            val=4,
            left=TreeNode(val=1),
            right=TreeNode(val=10)
            ),
        right=TreeNode(
            val=9,
            right=TreeNode(val=7)
            )
        )
    Solution().replaceValueInTree(root)
    assert root.left.left.val == 7
    assert root.left.right.val == 7
    assert root.right.right.val == 11


def test_2():
    root = TreeNode(
        val=3,
        left=TreeNode(val=1),
        right=TreeNode(val=2)
        )
    Solution().replaceValueInTree(root)
    assert root.val == 0
    assert root.left.val == 0
    assert root.left.val == 0


if __name__ == '__main__':
    test_1()
    test_2()
