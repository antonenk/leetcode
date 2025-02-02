#!/usr/bin/python3

# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
# beats 93% runtime / 79% mem

from leetcode import TreeNode


def getValuesFromTree(root: TreeNode):
    nodes = []
    node = root
    while node is not None or len(nodes) > 0:
        while node is not None:
            nodes.append(node)
            node = node.left
        node = nodes.pop()
        yield node.val
        node = node.right
    yield None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        gen1 = getValuesFromTree(root1)
        gen2 = getValuesFromTree(root2)

        result = []
        val1 = next(gen1)
        val2 = next(gen2)
        while val1 is not None and val2 is not None:
            if val1 < val2:
                result.append(val1)
                val1 = next(gen1)
            else:
                result.append(val2)
                val2 = next(gen2)

        while val1 is not None:
            result.append(val1)
            val1 = next(gen1)

        while val2 is not None:
            result.append(val2)
            val2 = next(gen2)

        return result


def test_1():
    root1 = TreeNode(
        val=2,
        left=TreeNode(val=1),
        right=TreeNode(val=4)
        )
    root2 = TreeNode(
        val=1,
        left=TreeNode(val=0),
        right=TreeNode(val=3)
        )
    assert Solution().getAllElements(root1, root2) == [0, 1, 1, 2, 3, 4]


def test_2():
    root1 = TreeNode(
        val=8,
        left=TreeNode(val=1)
        )
    root2 = TreeNode(
        val=1,
        right=TreeNode(val=8)
        )
    assert Solution().getAllElements(root1, root2) == [1, 1, 8, 8]


def test_0():
    root = TreeNode(
        val=100,
        left=TreeNode(
            val=50,
            left=TreeNode(
                val=25,
                left=TreeNode(val=12)
                ),
            right=TreeNode(
                val=75,
                left=TreeNode(val=70),
                right=TreeNode(val=80)
                )
            ),
        right=TreeNode(
            val=200,
            left=TreeNode(val=150),
            right=TreeNode(
                val=250,
                right=TreeNode(val=275)
                )
            )
        )
    gen = getValuesFromTree(root)
    val = next(gen)
    result = []
    while val is not None:
        result.append(val)
        val = next(gen)
    assert result == [12, 25, 50, 70, 75, 80, 100, 150, 200, 250, 275]


if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
