#!/usr/bin/python3

# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
# beats 100% runtime / 66% mem

from leetcode import TreeNode


def walkTree(depth: int, node: TreeNode) -> tuple[int, TreeNode]:
    if node.left is None:
        if node.right is None:
            return depth + 1, node
        else:
            return walkTree(depth + 1, node.right)
    else:
        if node.right is None:
            return walkTree(depth + 1, node.left)
        else:
            depthLeft, nodeLeft = walkTree(depth + 1, node.left)
            depthRight, nodeRight = walkTree(depth + 1, node.right)
            if depthLeft == depthRight:
                return depthLeft, node
            elif depthLeft > depthRight:
                return depthLeft, nodeLeft
            else:
                return depthRight, nodeRight


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        depth, node = walkTree(0, root)
        return node


def test_1():
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=1,
            left=TreeNode(val=6),
            right=TreeNode(
                val=2,
                left=TreeNode(val=7),
                right=TreeNode(val=4)
                )
            ),
        right=TreeNode(
            val=1,
            left=TreeNode(val=0),
            right=TreeNode(val=8)
            )
        )
    lca = Solution().lcaDeepestLeaves(root)
    assert lca.val == 2


if __name__ == '__main__':
    test_1()
