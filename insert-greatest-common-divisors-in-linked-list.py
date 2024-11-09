#!/usr/bin/python3

# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

from typing import Optional
from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curListNode = head
        while curListNode.next is not None:
            nextListNode = curListNode.next
            midListNode = ListNode(
                val=gcd(curListNode.val, nextListNode.val),
                next=nextListNode
                )
            curListNode.next = midListNode
            curListNode = nextListNode

        return head


def getArrayFromLinkedList(ln: ListNode):
    result = [ln.val]
    while ln.next is not None:
        ln = ln.next
        result.append(ln.val)
    return result


def getLinkedListFromArray(values: list):
    firstListNode = None
    prevListNode = None
    for value in values:
        curListNode = ListNode(val=value)
        if firstListNode is None:
            firstListNode = curListNode
        if prevListNode is not None:
            prevListNode.next = curListNode
        prevListNode = curListNode
    return firstListNode


def test_1():
    result = Solution().insertGreatestCommonDivisors(getLinkedListFromArray([18, 6, 10, 3]))
    assert getArrayFromLinkedList(result) == [18, 6, 6, 2, 10, 1, 3]


def test_2():
    result = Solution().insertGreatestCommonDivisors(getLinkedListFromArray([7]))
    assert getArrayFromLinkedList(result) == [7]


if __name__ == '__main__':
    test_2()
    test_1()
