#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 28% mem

from leetcode import TreeNode


def walkTree(node: TreeNode) -> tuple[int, int]:
    if node.left is not None:
        leftBalance, leftStepsNeeded = walkTree(node.left)
    else:
        leftBalance, leftStepsNeeded = 0, 0
    if node.right is not None:
        rightBalance, rightStepsNeeded = walkTree(node.right)
    else:
        rightBalance, rightStepsNeeded = 0, 0

    balance = leftBalance + rightBalance + node.val - 1
    stepsNeeded = leftStepsNeeded + rightStepsNeeded + abs(balance)
    return balance, stepsNeeded


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        return walkTree(root)[1]


def test_1():
    root = TreeNode(
        val=3,
        left=TreeNode(val=0),
        right=TreeNode(val=0)
        )
    assert Solution().distributeCoins(root) == 2


def test_2():
    root = TreeNode(
        val=0,
        left=TreeNode(val=3),
        right=TreeNode(val=0)
        )
    assert Solution().distributeCoins(root) == 3


def test_3():
    root = TreeNode(
        val=0,
        left=TreeNode(val=0),
        right=TreeNode(val=3)
        )
    assert Solution().distributeCoins(root) == 3


def test_4():
    root = TreeNode(
        val=0,
        left=TreeNode(
            val=0,
            left=TreeNode(
                val=0,
                left=TreeNode(
                    val=0,
                    left=TreeNode(val=5)
                    )
                )
            )
        )
    assert Solution().distributeCoins(root) == 10


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
