#!/usr/bin/python3

# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/
# Beats runtime 99%, mem 11%


class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        answers = []
        for query in queries:
            answer = 0
            square_radius = query[2] ** 2
            for point in points:
                square_distance = (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2
                if square_distance <= square_radius:
                    answer += 1
            answers.append(answer)
        return answers


def test_1():
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    assert Solution().countPoints(points, queries) == [3, 2, 2]


def test_2():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
    assert Solution().countPoints(points, queries) == [2, 3, 2, 4]


if __name__ == '__main__':
    test_1()
    test_2()
