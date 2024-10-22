#!/usr/bin/python3

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstListNode = ListNode()
        curListNode = firstListNode
        srcListNode = head.next
        while srcListNode.next is not None:
            if srcListNode.val == 0:
                nextListNode = ListNode()
                curListNode.next = nextListNode
                curListNode = nextListNode
            else:
                curListNode.val += srcListNode.val

            srcListNode = srcListNode.next

        return firstListNode


def getStringFromLinkedList(ln: ListNode):
    result = [str(ln.val)]
    while ln.next is not None:
        ln = ln.next
        result.append(str(ln.val))
    return ','.join(result)


def getLinkedListFromString(s: str):
    firstListNode = None
    prevListNode = None
    for element in s.split(','):
        curListNode = ListNode(val=int(element))
        if firstListNode is None:
            firstListNode = curListNode
        if prevListNode is not None:
            prevListNode.next = curListNode
        prevListNode = curListNode
    return firstListNode


def test_1():
    ln = getLinkedListFromString("0,3,1,0,4,5,2,0")
    assert getStringFromLinkedList(Solution().mergeNodes(ln)) == '4,11'


def test_2():
    ln = getLinkedListFromString("0,1,0,3,0,2,2,0")
    assert getStringFromLinkedList(Solution().mergeNodes(ln)) == '1,3,4'


if __name__ == '__main__':
    test_1()
    test_2()
