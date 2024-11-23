#!/usr/bin/python3

# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# beats 96% runtime / 24% mem

from typing import Optional
from leetcode import ListNode, getLinkedListFromArray


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = [head.val]
        while head.next is not None:
            head = head.next
            values.append(head.val)
        return max([values[i] + values[-1 - i] for i in range(len(values) // 2)])


def test_1():
    assert Solution().pairSum(getLinkedListFromArray([5, 4, 2, 1])) == 6


def test_2():
    assert Solution().pairSum(getLinkedListFromArray([4, 2, 2, 3])) == 7


def test_3():
    assert Solution().pairSum(getLinkedListFromArray([1, 100000])) == 100001


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
