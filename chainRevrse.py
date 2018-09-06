# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def add(self,val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            q = [self.head]
            while True:
                popNode = q.pop(0)
                if popNode.next is None:
                    popNode.next = node
                    return
                else:
                    q.append(popNode.next)

    def traversal(self, head):
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next

        return res

class S:
    def __init__(self):
        pass

    def listReverse(self,head):
        if head is None:
            return None

        if head.next is None:
            return head

        dummy = None
        while head is not None:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp

        return dummy

if __name__=='__main__':
    L = List()
    for i in range(1, 10):
        L.add(i)
    print 'traversal list:', L.traversal(L.head)

    S = S()
    rhead = S.listReverse(L.head)
    print 'reverse list', L.traversal(rhead)