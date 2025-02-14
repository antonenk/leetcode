#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 33% runtime / 64% mem

from typing import Any


class Node:
    def __init__(self, val: int, isLeaf: bool, topLeft: Any, topRight: Any, bottomLeft: Any, bottomRight: Any):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def constructTree(grid: list[list[int]], row: int, col: int, size: int):
    if size == 1:
        return Node(grid[row][col], True, None, None, None, None)
    else:
        size = size // 2
        topLeft = constructTree(grid, row, col, size)
        topRight = constructTree(grid, row, col + size, size)
        bottomLeft = constructTree(grid, row + size, col, size)
        bottomRight = constructTree(grid, row + size, col + size, size)
        sumVal = topLeft.val + topRight.val + bottomLeft.val + bottomRight.val
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and sumVal in (0, 4):
            return Node(topLeft.val, True, None, None, None, None)
        else:
            return Node(
                -1,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
                )


class Solution:
    def construct(self, grid: list[list[int]]):
        return constructTree(grid, 0, 0, len(grid))


def test_1():
    grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]]
    tree = Solution().construct(grid)
    assert tree.topLeft.isLeaf
    assert tree.bottomLeft.isLeaf
    assert tree.bottomRight.isLeaf
    assert tree.topRight.topLeft.isLeaf
    assert tree.topRight.topRight.isLeaf
    assert tree.topRight.bottomLeft.isLeaf
    assert tree.topRight.bottomRight.isLeaf


if __name__ == '__main__':
    test_1()
