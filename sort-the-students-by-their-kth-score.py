#!/usr/bin/python3

# https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
# beats 100% runtime / 98% mem


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        score.sort(reverse=True, key=lambda s: s[k])
        return score


def test_1():
    score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    sort2 = [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]
    assert Solution().sortTheStudents(score, 2) == sort2


def test_2():
    score = [[3, 4], [5, 6]]
    sort0 = [[5, 6], [3, 4]]
    assert Solution().sortTheStudents(score, 0) == sort0


if __name__ == '__main__':
    test_1()
    test_2()
