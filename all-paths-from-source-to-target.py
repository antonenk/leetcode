#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 39% runtime / 6% mem


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        pathsToTarget = []
        target = len(graph) - 1
        paths = [[0]]
        while len(paths) > 0:
            newPaths = []
            for path in paths:
                lastNode = path[-1]
                for nextStep in graph[lastNode]:
                    newPath = path.copy()
                    newPath.append(nextStep)
                    if nextStep == target:
                        pathsToTarget.append(newPath)
                    else:
                        newPaths.append(newPath)
            paths = newPaths
        return pathsToTarget


def test_1():
    graph = [[1, 2], [3], [3], []]
    output = Solution().allPathsSourceTarget(graph)
    expected = [[0, 1, 3], [0, 2, 3]]
    assert output == expected


def test_2():
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    output = Solution().allPathsSourceTarget(graph)
    expected = [
        [0, 4],
        [0, 3, 4],
        [0, 1, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 3, 4]
        ]
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
