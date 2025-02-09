#!/usr/bin/python3

# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
# beats 82% runtime / 29% mem

from leetcode import TreeNode


def walkTree(node: TreeNode, values: set[int], newValue: int):
    values.add(newValue)
    if node.left is not None:
        walkTree(node.left, values, 2 * newValue + 1)
    if node.right is not None:
        walkTree(node.right, values, 2 * newValue + 2)


class FindElements:
    def __init__(self, root: TreeNode):
        self.values: set[int] = set()
        walkTree(root, self.values, 0)

    def find(self, target: int) -> bool:
        return target in self.values


def test_1():
    root = TreeNode(
        val=-1,
        right=TreeNode(val=-1)
        )
    elements = FindElements(root)
    assert not elements.find(1)
    assert elements.find(2)


def test_2():
    root = TreeNode(
        val=-1,
        left=TreeNode(
            val=-1,
            left=TreeNode(val=-1),
            right=TreeNode(val=-1)
            ),
        right=TreeNode(val=-1)
        )
    elements = FindElements(root)
    assert elements.find(1)
    assert elements.find(3)
    assert not elements.find(5)


def test_3():
    root = TreeNode(
        val=-1,
        right=TreeNode(
            val=-1,
            left=TreeNode(val=-1)
            ),
        )
    elements = FindElements(root)
    assert elements.find(2)
    assert not elements.find(3)
    assert not elements.find(4)
    assert elements.find(5)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
