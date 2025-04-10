#!/usr/bin/python3

# https://leetcode.com/problems/all-possible-full-binary-trees/description/
# beats 59% runtime / 99% mem

from leetcode import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n % 2 == 0:
            return []
        fbts: list[list[TreeNode]] = [
            [],
            [TreeNode(val=0)],
            [],
            [TreeNode(val=0, left=TreeNode(val=0), right=TreeNode(val=0))]
        ]
        if n < 5:
            return fbts[n]
        for nodesCount in range(5, n + 1, 2):
            trees = []
            for countLeft in range(1, nodesCount, 2):
                for leftTree in fbts[countLeft]:
                    for rightTree in fbts[nodesCount - countLeft - 1]:
                        trees.append(TreeNode(val=0, left=leftTree, right=rightTree))
            fbts.append([])
            fbts.append(trees)

        return fbts[n]


def test_1():
    output = Solution().allPossibleFBT(7)
    assert len(output) == 5


def test_2():
    output = Solution().allPossibleFBT(3)
    assert len(output) == 1


def test_3():
    output = Solution().allPossibleFBT(5)
    assert len(output) == 2


def test_4():
    output = Solution().allPossibleFBT(100)
    assert len(output) == 0


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
