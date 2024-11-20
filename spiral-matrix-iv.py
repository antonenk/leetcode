#!/usr/bin/python3

# https://leetcode.com/problems/spiral-matrix-iv/description/
# beats 78% runtime / 48% mem

from typing import Optional
from leetcode import ListNode, getArrayFromLinkedList, getLinkedListFromArray


def numsFromList(head: ListNode):
    while True:
        yield head.val
        head = head.next
        if head is None:
            break


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        result = [[-1] * n for i in range(m)]

        nums = numsFromList(head)
        rMin = 0
        rMax = m - 1
        cMin = 0
        cMax = n - 1

        try:
            while rMin <= rMax and cMin <= cMax:
                for c in range(cMin, cMax + 1):
                    result[rMin][c] = next(nums)
                rMin += 1

                for r in range(rMin, rMax + 1):
                    result[r][cMax] = next(nums)
                cMax -= 1

                for c in range(cMax, cMin - 1, -1):
                    result[rMax][c] = next(nums)
                rMax -= 1

                for r in range(rMax, rMin - 1, -1):
                    result[r][cMin] = next(nums)
                cMin += 1
        except StopIteration:
            pass

        return result


def test_1():
    head = getLinkedListFromArray([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
    output = [
        [3, 0,  2,  6, 8],
        [5, 0, -1, -1, 1],
        [5, 2,  4,  9, 7]
        ]
    assert Solution().spiralMatrix(3, 5, head) == output


def test_2():
    head = getLinkedListFromArray([0, 1, 2])
    output = [[0, 1, 2, -1]]
    assert Solution().spiralMatrix(1, 4, head) == output


if __name__ == '__main__':
    test_1()
    test_2()
