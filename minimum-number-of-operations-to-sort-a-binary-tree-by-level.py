#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 5% runtime / 98% mem

from leetcode import TreeNode


class Solution:
    def minimumOperations(self, root: TreeNode) -> int:
        prevLevel = [root]
        swapsCount = 0
        while len(prevLevel) > 0:
            curLevel = []
            for node in prevLevel:
                if node.left is not None:
                    curLevel.append(node.left)
                if node.right is not None:
                    curLevel.append(node.right)
            values = [node.val for node in curLevel]
            sortedValues = sorted(values)
            for index in range(len(sortedValues)):
                value = values[index]
                sortedValue = sortedValues[index]
                if value != sortedValue:
                    swapsCount += 1
                    swapIndex = values.index(sortedValue)
                    values[swapIndex] = value
                    values[index] = sortedValue
            prevLevel = curLevel
        return swapsCount


def test_1():
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=4,
            left=TreeNode(val=7),
            right=TreeNode(val=6)
            ),
        right=TreeNode(
            val=3,
            left=TreeNode(
                val=8,
                left=TreeNode(val=9)
                ),
            right=TreeNode(
                val=5,
                left=TreeNode(val=10)
                )
            )
        )
    assert Solution().minimumOperations(root) == 3


def test_2():
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=3,
            left=TreeNode(val=7),
            right=TreeNode(val=6)
            ),
        right=TreeNode(
            val=2,
            left=TreeNode(val=5),
            right=TreeNode(val=4)
            )
        )
    assert Solution().minimumOperations(root) == 3


def test_3():
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=4),
            right=TreeNode(val=5)
            ),
        right=TreeNode(
            val=3,
            left=TreeNode(val=6)
            )
        )
    assert Solution().minimumOperations(root) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
