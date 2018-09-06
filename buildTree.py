# -*- coding: utf-8 -*-


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                popNode = q.pop(0)
                if popNode.left is None:
                    popNode.left = node
                    return
                elif popNode.right is None:
                    popNode.right = node
                    return
                else:
                    q.append(popNode.left)
                    q.append(popNode.right)

if __name__=='__main__':
    T = Tree()
    for i in range(1,10,1):
        T.add(i)
    print T.root.val