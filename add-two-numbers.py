#!/usr/bin/python3

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstListNode = None
        prevListNode = None
        overflow = 0
        while True:
            l1Digit = 0 if l1 is None else l1.val
            l2Digit = 0 if l2 is None else l2.val
            sum = l1Digit + l2Digit + overflow
            digit = sum % 10
            overflow = 1 if sum >= 10 else 0
            curListNode = ListNode(val=digit)
            if firstListNode is None:
                firstListNode = curListNode
            if prevListNode is not None:
                prevListNode.next = curListNode
            prevListNode = curListNode

            if l1 is None or l1.next is None:
                l1 = None
            else:
                l1 = l1.next

            if l2 is None or l2.next is None:
                l2 = None
            else:
                l2 = l2.next

            if l1 is None and l2 is None and overflow == 0:
                break

        return firstListNode


def getStringFromLinkedList(ln: ListNode):
    result = str(ln.val)
    while ln.next is not None:
        ln = ln.next
        result = str(ln.val) + result
    return result


def getLinkedListFromString(s: str):
    digits = [int(c) for c in s]
    digits.reverse()
    firstListNode = None
    prevListNode = None
    for digit in digits:
        curListNode = ListNode(val=digit)
        if firstListNode is None:
            firstListNode = curListNode
        if prevListNode is not None:
            prevListNode.next = curListNode
        prevListNode = curListNode
    return firstListNode


def test_1():
    l1 = getLinkedListFromString("342")
    l2 = getLinkedListFromString("465")
    assert getStringFromLinkedList(Solution().addTwoNumbers(l1, l2)) == '807'


def test_2():
    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    assert getStringFromLinkedList(Solution().addTwoNumbers(l1, l2)) == '0'


def test_3():
    l1 = getLinkedListFromString("9999999")
    l2 = getLinkedListFromString("9999")
    assert getStringFromLinkedList(Solution().addTwoNumbers(l1, l2)) == '10009998'


if __name__ == '__main__':
    test_2()
    test_1()
    test_3()
