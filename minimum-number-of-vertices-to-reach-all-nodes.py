#!/usr/bin/python3

# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
# beats 73% runtime / 68% mem


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        reachable = [False] * n
        for edge in edges:
            reachable[edge[1]] = True
        return [i for i in range(n) if not reachable[i]]


def test_1():
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    expected = [0, 3]
    output = Solution().findSmallestSetOfVertices(n, edges)
    assert output == expected


def test_2():
    n = 5
    edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    expected = [0, 2, 3]
    output = Solution().findSmallestSetOfVertices(n, edges)
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
