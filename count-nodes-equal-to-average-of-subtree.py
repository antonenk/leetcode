#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 48% runtime / 16% mem

from typing import Tuple
from leetcode import TreeNode


def walkTree(node: TreeNode) -> Tuple[int, int, int]:
    if node.left is not None:
        left_total_sum, left_total_count, left_suitable_count = walkTree(node.left)
    else:
        left_total_sum = left_total_count = left_suitable_count = 0

    if node.right is not None:
        right_total_sum, right_total_count, right_suitable_count = walkTree(node.right)
    else:
        right_total_sum = right_total_count = right_suitable_count = 0

    total_sum = left_total_sum + right_total_sum + node.val
    total_count = left_total_count + right_total_count + 1
    suitable_count = left_suitable_count + right_suitable_count
    if total_sum // total_count == node.val:
        suitable_count += 1
    return total_sum, total_count, suitable_count


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total_sum, total_count, suitable_count = walkTree(root)
        return suitable_count


def test_1():
    root = TreeNode(
        val=4,
        left=TreeNode(
                val=8,
                left=TreeNode(val=0),
                right=TreeNode(val=1)
            ),
        right=TreeNode(
            val=5,
            right=TreeNode(val=6)
            )
        )
    assert Solution().averageOfSubtree(root) == 5


def test_2():
    assert Solution().averageOfSubtree(TreeNode(val=1)) == 1


if __name__ == '__main__':
    test_1()
    test_2()
