#!/usr/bin/python3

# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# beats 8% runtime / 48% mem

from leetcode import ListNode, getArrayFromLinkedList, getLinkedListFromArray


class Solution:
    def deleteNode(self, node):
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next


def test_1():
    secondNode = getLinkedListFromArray([5, 1, 9])
    head = ListNode(4)
    head.next = secondNode
    Solution().deleteNode(secondNode)
    assert getArrayFromLinkedList(head) == [4, 1, 9]


if __name__ == '__main__':
    test_1()
