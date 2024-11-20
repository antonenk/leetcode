class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
