#!/usr/bin/python3

# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
# beats 7% runtime / 32% mem

from leetcode import ListNode, getLinkedListFromArray, getArrayFromLinkedList


class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        node = head
        resultArray: list[int] = []
        while node is not None:
            value = node.val
            while len(resultArray) > 0 and resultArray[-1] < value:
                resultArray.pop()
            resultArray.append(value)
            node = node.next

        firstListNode = None
        prevListNode = None
        for value in resultArray:
            curListNode = ListNode(val=value)
            if firstListNode is None:
                firstListNode = curListNode
            if prevListNode is not None:
                prevListNode.next = curListNode
            prevListNode = curListNode

        return firstListNode


def test_1():
    head = getLinkedListFromArray([5, 2, 13, 3, 8])
    assert getArrayFromLinkedList(Solution().removeNodes(head)) == [13, 8]


def test_2():
    head = getLinkedListFromArray([1, 1, 1, 1])
    assert getArrayFromLinkedList(Solution().removeNodes(head)) == [1, 1, 1, 1]


if __name__ == '__main__':
    test_1()
    test_2()
