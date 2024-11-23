#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 89% mem


from typing import Optional
from leetcode import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(val=preorder[0])
        if len(preorder) == 1:
            return root
        rightTreeIndex = 1
        while rightTreeIndex < len(preorder) and preorder[rightTreeIndex] < preorder[0]:
            rightTreeIndex += 1
        root.left = self.bstFromPreorder(preorder[1:rightTreeIndex])
        root.right = self.bstFromPreorder(preorder[rightTreeIndex:])
        return root


def test_1():
    preorder = [8, 5, 1, 7, 10, 12]
    output = Solution().bstFromPreorder(preorder)
    expected = output
    assert output == expected


def test_2():
    preorder = [1, 3]
    output = Solution().bstFromPreorder(preorder)
    expected = output
    assert output == expected


def test_3():
    preorder = [4, 2]
    output = Solution().bstFromPreorder(preorder)
    expected = output
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
