#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 95% runtime / 37% mem

from leetcode import ListNode, getArrayFromLinkedList, getLinkedListFromArray


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cNode = list2
        while cNode.next is not None:
            cNode = cNode.next
        aNode = list1
        for i in range(a - 1):
            aNode = aNode.next
        bNode = aNode
        for i in range(b - a + 2):
            bNode = bNode.next
        aNode.next = list2
        cNode.next = bNode
        return list1


def test_1():
    list1 = getLinkedListFromArray([10, 1, 13, 6, 9, 5])
    a = 3
    b = 4
    list2 = getLinkedListFromArray([1000000, 1000001, 1000002])
    output = getArrayFromLinkedList(Solution().mergeInBetween(list1, a, b, list2))
    expected = [10, 1, 13, 1000000, 1000001, 1000002, 5]
    assert output == expected


def test_2():
    list1 = getLinkedListFromArray([0, 1, 2, 3, 4, 5, 6])
    a = 2
    b = 5
    list2 = getLinkedListFromArray([1000000, 1000001, 1000002, 1000003, 1000004])
    output = getArrayFromLinkedList(Solution().mergeInBetween(list1, a, b, list2))
    expected = [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
