#!/usr/bin/python3

# https://leetcode.com/problems/all-possible-full-binary-trees/description/
# beats 5% runtime / 5% mem

from leetcode import TreeNode


def allFBT(n: int) -> list[TreeNode]:
    if n == 1:
        return [TreeNode(val=0)]
    elif n == 3:
        return [TreeNode(val=0, left=TreeNode(val=0), right=TreeNode(val=0))]
    else:
        trees = []
        for countLeft in range(1, n, 2):
            leftTrees = allFBT(countLeft)
            for leftTree in leftTrees:
                rightTrees = allFBT(n - countLeft - 1)
                for rightTree in rightTrees:
                    trees.append(TreeNode(val=0, left=leftTree, right=rightTree))
        return trees


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        return allFBT(n)


def test_1():
    output = Solution().allPossibleFBT(7)
    assert len(output) == 5


def test_2():
    output = Solution().allPossibleFBT(3)
    assert len(output) == 1


def test_3():
    output = Solution().allPossibleFBT(5)
    assert len(output) == 2


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
