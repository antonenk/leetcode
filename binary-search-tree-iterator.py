#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 20% runtime / 19% mem

from leetcode import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.parents = []
        node = root
        while node is not None:
            self.parents.append([node, False])
            node = node.left

    def next(self) -> int:
        nodeInfo = self.parents[-1]
        node: TreeNode = nodeInfo[0]  # type: ignore
        result = node.val
        nodeInfo[1] = True

        if node.right is not None:
            node = node.right
            while node is not None:
                self.parents.append([node, False])
                node = node.left
        else:
            while len(self.parents) > 0 and self.parents[-1][1]:
                self.parents.pop()

        return result

    def hasNext(self) -> bool:
        return len(self.parents) > 0


def test_1():
    root = TreeNode(
        val=7,
        left=TreeNode(val=3),
        right=TreeNode(
            val=15,
            left=TreeNode(val=9),
            right=TreeNode(val=20)
            )
        )
    bSTIterator = BSTIterator(root)
    assert bSTIterator.next() == 3
    assert bSTIterator.next() == 7
    assert bSTIterator.hasNext()
    assert bSTIterator.next() == 9
    assert bSTIterator.hasNext()
    assert bSTIterator.next() == 15
    assert bSTIterator.hasNext()
    assert bSTIterator.next() == 20
    assert not bSTIterator.hasNext()


if __name__ == '__main__':
    test_1()
